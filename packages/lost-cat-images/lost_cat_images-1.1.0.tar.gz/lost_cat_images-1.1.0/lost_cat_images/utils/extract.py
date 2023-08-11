""""""
from datetime import datetime
import logging
import cv2 as cv
import numpy as np
import requests
import os
import time

from lost_cat_images.utils.utils_boxes import process_box_contours, process_box_templates
from lost_cat_images.utils.utils_graphics import draw_ellipse, ellipse_fitting, ellipse_ocr_link, remove_text_from_image, line_filtering, line_ocr_link, draw_line
from lost_cat_images.utils.utils_grids import process_grids
from lost_cat_images.utils.utils_ocr_engines import ocr_azure, ocr_tesseract
from lost_cat_images.utils.utils_rules import process_ellipses, process_shaperules, process_shapes

logger = logging.getLogger(__name__)

def extract_contours(image: object, config: dict = None) -> dict:
    """ Processes the image and returns the edges of the objects found.

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
        mode: int default cv.RETR_TREE 3
            OpenCV RetrievalModes
            cv.RETR_EXTERNAL
                retrieves only the extreme outer contours. It sets
                hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
            cv.RETR_LIST
                retrieves all of the contours without establishing any hierarchical relationships.
            cv.RETR_CCOMP
                retrieves all of the contours and organizes them into a two-level hierarchy.
                At the top level, there are external boundaries of the components.
                At the second level, there are boundaries of the holes. If there is another
                contour inside a hole of a connected component, it is still put at the top level.
            cv.RETR_TREE
                retrieves all of the contours and reconstructs a full hierarchy of nested contours.
            cv.RETR_FLOODFIL
        method: int default cv.CHAIN_APPROX_SIMPLE 2
            OpenCV ContourApproximationModes
            cv.CHAIN_APPROX_NONE
                stores absolutely all the contour points. That is, any 2 subsequent points
                (x1,y1) and (x2,y2) of the contour will be either horizontal, vertical or
                diagonal neighbors, that is, max(abs(x1-x2),abs(y2-y1))==1.
            cv.CHAIN_APPROX_SIMPLE
                compresses horizontal, vertical, and diagonal segments and leaves only their
                end points. For example, an up-right rectangular contour is encoded with 4 points.
            cv.CHAIN_APPROX_TC89_L1
                applies one of the flavors of the Teh-Chin chain approximation algorithm [209]
            cv.CHAIN_APPROX_TC89_KCOS
                applies one of the flavors of the Teh-Chin chain approximation algorithm [209]
        offset: point
            A point to
        image: np.array
            an image to use for markup

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    data = {
        "images": {},
        "data": {},
    }

    markup_image = config.get("image") if config else None
    mode = config.get('mode', cv.RETR_TREE) if config else cv.RETR_TREE
    method = config.get('method', cv.CHAIN_APPROX_SIMPLE) if config else cv.CHAIN_APPROX_SIMPLE

    if len(image.shape) == 3:
        result = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        # img_test = cv2.cvtColor(img_color_seg, cv2.COLOR_RGB2GRAY)
    elif len(image.shape) == 2:
        result = image
    else:
        print("May have wrong input")
        data['errors'] = []
        data['errors'].append(f'invalid image format {image.shape}')
        return data

    contours, _ = cv.findContours(image=result, mode=mode, method=method)
    if markup_image is not None:
        cv.drawContours(markup_image, contours=contours, contourIdx=-1, color=(255, 0, 255), thickness= 1)
        data["images"]["markup"] = markup_image

    data['data']['contours'] = contours
    return data

def boxes(image: object, config: dict = None) -> dict:
    """ Discovers and produces a list of boxes aligned in
    the horzontal and vertical orientation in the image

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A dictionary of params for the function
        'engine'    : the engine to use [contour | template]
        'minsize'   : the smallest shape to return
        'threshold' : (optional) set the detection level
        'image'     : (optional) a markup image to apply to markup to

        for 'contour':
            'kernelsize': int default 5
            'step': int matching corner bleed

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            'processed': np.array

        data: dict
            'shapes': dict
                'idx'   : indexx for the shape
                'origin': (x,y)
                'bbox'  : (x,y,w,h)
        }
    """
    engines = {
        'contour': process_box_contours,
        'template': process_box_templates,
    }

    engine = config.get('engine', 'contour') if config else 'contour'
    logger.info('Boxes Engine: %s', engine)
    data = {}
    # get the shapes from the contours
    try:
        data = engines[engine](image=image, config=config)
    except Exception as ex:
        logger.error('boxes: engine: %s ex: %s', engine, ex)
        return {
            'errors': f'General error for [{engine}]: {ex}'
        }

    return data

def grids(image: object, config: dict = None) -> dict:
    """ will return the grids found in the image and the associated contents

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
        graph: nx.Graph
        shapes: dict
            a dict of the shapes found
            idx     : int shape index
            origin  : (x,y)
            bbox    : (x,y,w,h)
            contour : list of points
            conf    : float the confidence the box is a box
        text: dict
            a dict of the text areas found
            idx:
            origin  : (x,y)
            bbox    : (x,y,w,h)
            contour : list of points
            text    : the text found
            conf    : float the confidence the text is correct

    Returns
    -------
    dict:
        'images': dict
            'candidates':
                image markuped with groups and shapes
            'groups':
                image markuped with graph joins
        'data': dict
            'shapes':
                list of shapes
            'graph':
                the graph of the shapes
            'grids':
                the found grids
            'tables':
                the table details
            'mapping':
                the mapping of shapes to text
    """
    data = {
        "images": {
            "processed": None
        },
        "data": {},
    }

    # get the grid for the shapes...
    engine = config.get('engine','basic') if config else 'basic'

    engines = {
        'basic': process_grids
    }

    if func := engines.get(engine):
        return func(image=image, config=config)
    else:
        return data

def analyze(image: object, config: dict = None) -> dict:
    """ Will analyze an image and provide a summary of the image,
    the current idea for the analysis are as follows

    Channel distribution - used to calculate threshold, and segmentation values
    Channel histogram - a histogram per channelother useful features
    Caveat: the analysis process should be as fast as possible

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
        mode: int
            OpenCV RetrievalModes
        method: int
            OpenCV ContourApproximationModes
        offset: point
            A point to

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    data = {
        "images": {
            "processed": None
        },
        "data": {},
    }

    # code here...

    return data

def text(image: object, config: dict = None) -> dict:
    """ Will use the declared engines to return the text from the image.

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A dictionary of params for the function
        engine: list
            ['azure', 'tesseract', 'doctr']...
        params: dict
            'azure': dict
                use_cache: bool
                    To prevent from consuming credits again for the
                    same image file when developing, set `use_cache` as True.
                    Otherwise, if you want to use Azure to detect
                    text again, set it as False.
              {'azure':{param: value, ...}, 'tesseract':{{param: value, ...}}

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            texts: list
                word_cluster: str
                words: dict
    """
    engines = {
        'azure': ocr_azure,
        'tesseract': ocr_tesseract,
    }

    engine = config.get('engine', 'azure') if config else 'azure'
    logger.info('Boxes Engine: %s', engine)
    data = {}
    # get the shapes from the contours
    try:
        data = engines[engine](image=image, config=config)
    except Exception as ex:
        logger.error('boxes: engine: %s ex: %s', engine, ex)
        return {
            'errors': f'General error for [{engine}]: {ex}'
        }

    return data

def run_rules(image: object, config: dict = None) -> dict:
    """ will return the grids found in the image and the associated contents

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
        graph: nx.Graph
            invludes the text elements


    """
    data = {
        "images": {
            "processed": None
        },
        "data": {},
    }

    # get the grid for the shapes...
    word_data = config.get("words", {})
    shape_data = config.get("shapes", {})
    mapping_data = config.get("mapping", {})
    rules_data = config.get("rules", {})
    ellipse_data = config.get("ellipses", {})
    export_data = config.get("export", {})

    # load a lookup for the shapes...
    # this will get the phrase in each shape,
    shape_lookup = process_shapes(shapes=shape_data, words=word_data, mappings=mapping_data)

    # now process the tables...
    rules_results = process_shaperules(shape_lookup=shape_lookup, rules_data=rules_data)

    data['data']['detail'] = rules_results.get('rule_run')
    data['data']['shapes'] = rules_results.get('shapes')

    data['data']['ellipses'] = process_ellipses(ellipses=ellipse_data)

    return data

def circles(image: object,
            config: dict = None) -> dict:
    """ Will use the hough transformation method to detect the circles from the image.

    Parameters
    ----------
    `image`: object
        Accepts an image object. Highly recommend to use a DENOISED/BLURRED image object to increase accuracy.
    `config`: dict
        A dictionary of params for the function
        - `engine`: list \n
            the engine to use \n
            ['hough', 'blob', 'contour']...
        - `params`: dict
            - 'hough': dict
                - 'method'      : int
                - 'dp'          : int, dpi
                - 'minDist'     : int, the minimum distance between circles
                - 'param1'      : int, higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller)
                - 'param2'      : int, accumulator threshold for the circle centers. The smaller it is, the more false circles may be detected.
                - 'minRadius'   : int, the smallest radius to detect
                - 'maxRadious'  : int, the largest radius to detect
            - 'image' : (optional) a markup image to apply to markup to

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
            markup: (optional) np.array
        data: dict
            shapes: list
                idx: int
                source: str
                type:  string / enum 'circle' the shape type
                bbox: dict a rectangular bounding box of the shape
                    x: numeric
                    y: numeric
                    r: numeric
                confidence: (optional) double
    """
    engines = {
        'hough':'a_function'
    }
    data = {
        "images":{
            "markup":None
        },
        "data":{
            "shapes":[]
        }
    }
    image = np.array(image).copy()
    markup_image = config.get("image")
    method = config.get("method",3)
    dp = config.get("dp",1)
    minDist = config.get("minDist",30)
    param1 = config.get("param1",100)
    param2 = config.get("param2",60)
    minRadius = config.get("minRadius",28)
    maxRadius = config.get("maxRadius",150)

    if image.shape.__len__() == 3:
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    circles = cv.HoughCircles(image,
                              method=method,
                              dp= dp,
                              minDist= minDist,
                              param1= param1,
                              param2= param2,
                              minRadius= minRadius,
                              maxRadius= maxRadius)
    circles = np.round(circles[0, :]).astype("int")
    data['data']['raw'] = circles

    for cidx, circle in enumerate(circles):
        x,y,z = circle
        data['data']['shapes'].append(
            {
            "idx":cidx,
            "source":"cv.HoughCircles",
            "type":"circle",
            "bbox":{
                "x":x, 'y':y, 'r':z
                }
            }
        )

    if markup_image is not None:
        for cidx,(x, y, r) in enumerate(circles):
            cv.circle(markup_image, (x, y), r, (0, 255, 0), 3)
            cv.putText(markup_image,
                       str(cidx),
                       org=(x,y),
                       fontScale=1,
                       color=(255, 0, 0),
                       thickness=2,
                       fontFace=cv.LINE_AA)
        data["images"]["markup"] = markup_image

    return data

def ellipse(
        image: object,
        config: dict = None
        ) -> dict :
    """
    Will fit the contour to detect ellipses from the image.
    This function will remove text from image to improve accuracy of ellipse detection.

    Parameters
    ----------
    `image`: object
        Accepts an image object. Highly recommend to use a binarized image object.

    `config`: dict
        A dictionary of params for the function
        - text_box_scale_ratio : 0.85
        - edge_detection_threshold
            - threshold1: 50
            - threshold2: 150
        - texts: dict
        - contours
            - mode: 0
            - method:2
        - filters - used to filter irrelevant contours
            - contour_length: 10
            - inertia_ratio: 0.5
            - area: 3000
            - min_adjacent_distance: 13

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            text_removed: np.ndarray
            markup: (optional) np.ndarray
        data: dict
            ellipses: list
                ellipse_idx: int
                center: (int, int) representing (x,y)
                size: (int, int) representing length of axes
                angle: int
                texts: list
                    text_idx: int
                    text: str
                    bounding Box: list of arrays
                    center: (int, int)
    """
    data = {
        "images":{
            "text_removed" : None,
            "markup":None
        },
        "data":{
            "ellipses":[]
        }
    }
    texts = config.get('texts', [])
    markup_image = config.get('image', None) if config else None

    config["bbox"] = np.array([word['boundingBox'] for d in texts for word in d['words']],
                              dtype=np.int32) # select all bounding boxes
    logger.info("BBox: %s %s", type(config["bbox"]), len(config.get("bbox", [])))

    config["words"] = [word['text'] for d in texts for word in d['words']] # select all texts
    logger.info("Words: %s %s", type(config["words"]), len(config.get("words",[])))


    img_text_removed = remove_text_from_image(image, config) # to improve accuracy of detecting
    ellipse_list = ellipse_fitting(img_text_removed, config)
    ellipse_data = ellipse_ocr_link(ellipse_list, config)
    data['data']['ellipses'] = ellipse_data

    if markup_image is not None:
        markup_image = config.get("image")
        img_ellipse = draw_ellipse(markup_image, ellipse_data)
        data['images']['markup'] = img_ellipse
        data['images']['text_removed'] = img_text_removed

    return data

def line(
        image: object,
        config: dict = None
        ) -> dict :
    """
    Will use Hough transformation to detect lines from the image.
    This function will remove text from image to improve accuracy of ellipse detection.

    Parameters
    ----------
    `image`: object
        Accepts an image object. Highly recommend to use a binarized image object.

    `config`: dict
        A dictionary of params for the function
            "text_box_scale_ratio":1.1,
            "threshold_type":9,
            "iterate":2,
            "max_area":3000,
            "max_angle_diff":7,
            "max_spd":3,
            "min_dist_to_line":10,
            "same_line_max_area":3000,
            "same_line_max_angle_diff":7,
            "same_line_max_spd":3

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            text_removed: np.ndarray
            markup: (optional) np.ndarray
        data: dict
            lines: list
                line_idx: int
                line: np.ndarray
                texts: list
                    text_idx: int
                    text: str
                    bounding Box: list of arrays
    """
    data = {
        "images":{
            "text_removed" : None,
            "markup":None
        },
        "data":{
            "lines":[]
        }
    }

    texts = config.get('texts', []) if config else None
    markup_image = config.get('image', None) if config else None
    threshold_type = config.get("threshold_type", 9) if config else cv.THRESH_BINARY_INV + cv.THRESH_OTSU
    hough_threshold = config.get("hough_threshold", 150) if config else 150
    hough_min_length = config.get("hough_min_length", 70) if config else 70
    hough_max_gap = config.get("hough_max_gap", 10) if config else 10

    if texts is not None:
        config["bbox"] = np.array([word['boundingBox'] for d in texts for word in d['words']],
                                dtype=np.int32) # select all bounding boxes
        logger.info("BBox: %s %s", type(config["bbox"]), len(config.get("bbox", [])))

        config["words"] = [word['text'] for d in texts for word in d['words']] # select all texts
        logger.info("Words: %s %s", type(config["words"]), len(config.get("words",[])))

        img_text_removed = remove_text_from_image(image, config) # to improve accuracy of detecting
    else:
        img_text_removed = image.copy()
    _, threshold = cv.threshold(img_text_removed, 0, 255, type = threshold_type)

    # line detection
    lines = cv.HoughLinesP(threshold, 1, np.pi / 180, threshold=hough_threshold, minLineLength=hough_min_length, maxLineGap=hough_max_gap)
    line_list = lines.squeeze()
    # filter lines
    line_list = line_filtering(line_list, config)
    line_data = line_ocr_link(line_list, config)
    data['data']['lines'] = line_data

    if markup_image is not None:
        markup_image = config.get("image")
        img_lines = draw_line(markup_image, line_data)
        data['images']['markup'] = img_lines
        data['images']['text_removed'] = img_text_removed

    return data
