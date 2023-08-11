""""""
from datetime import datetime
import logging
import cv2 as cv
import numpy as np
import skimage.morphology
import re
import skimage.morphology

from scipy.ndimage import rotate as scipy_rotate

from lost_cat_images.utils import convert_image
from lost_cat_images.utils.utils_image import bestangle

logger = logging.getLogger(__name__)

def color_segmentation(image: object, config: dict = None) -> dict:
    """ Using a HSV color space, set a range of values to mask the
    source image to remove both the sun bleaching and water damage areas

    Parameters
    ----------
    image: object
        Accepts an image object, Needs to be HSV
    config: dict
        A doctionary of params for the function

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array (RGB)
        data: dict
            None
    """
    data = {
        "images": {},
        "data": {},
    }
    images = []
    image =  np.array(image).copy()

    sourcetype = config.get("sourcetype", "bgr").lower() if config else "bgr"

    if sourcetype != "hsv":
        config_st = {
            "source": sourcetype,
            "dest": "hsv"
        }
        cnvt_data = convert_image(image=image, config=config_st)
        image = cnvt_data.get("images", {}).get("processed").copy()
        images.append({"hsv.orig": image.copy()})

    data['data']['masks'] = []
    # generate mask from config
    ranges = config.get('ranges', []) if config else []
    for range_id, range_val in enumerate(ranges):
        min_values = range_val.get('min')
        if isinstance(min_values, tuple):
            lower_bound = min_values
        elif isinstance(min_values, dict):
            lower_bound = (min_values['h'], min_values['s'], min_values['v'])

        max_values = range_val.get('max')
        if isinstance(max_values, tuple):
            upper_bound = max_values
        elif isinstance(max_values, dict):
            upper_bound = (max_values['h'], max_values['s'], max_values['v'])

        mask = cv.inRange(image, lower_bound, upper_bound)
        data['images'][f'mask_{range_id+1}'] = mask
        data['data']['masks'].append(f'mask_{range_id+1}')

    regex_pattern = r'^mask'
    mask_keys = [key for key in data['images'].keys() if re.match(regex_pattern, key)]
    logger.info("Mask Keys: %s", mask_keys)

    final_mask = sum(data['images'][key] for key in mask_keys)
    data['images']['final'] = final_mask

    logger.info("Result: Img: %s : %s Mask: %s : %s", image.shape, type(image), final_mask.shape, type(final_mask))

    # final_mask = sum(data['images'].values()) if data['images'].keys()
    result = cv.bitwise_and(image, image, mask=cv.bitwise_not(final_mask))

    # convert back as needed
    if sourcetype != "hsv":
        config_st = {
            "source": "hsv",
            "dest": sourcetype,
        }
        images.append({"hsv.filter": result.copy()})
        cnvt_data = convert_image(image=result, config=config_st)
        result = cnvt_data.get("images", {}).get("processed")

    result[np.where(result == [0])] = [255]

    images.append({"processed": result})
    logger.info("Results: %s", result.shape)

    for img_data in images:
        for k,v in img_data.items():
            data["images"][k] = v

    return data

def denoise(image: object, config: dict = None) -> dict:
    """ Remove typical types of noise from an image, for example; lone pixels.

    https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    image =  np.array(image).copy()
    mode = config.get('mode', 'bilateral') if config else 'bilateral'

    errors = []
    img_result = None

    if mode == 'bilateral':
        diameter = config.get('diameter', 9) if config else 9
        sigmac = config.get('sigmacolor', 75) if config else 75
        sigmas = config.get('sigmaspace', 75) if config else 75

        # noise deduction
        img_result = cv.bilateralFilter(image, d = diameter, sigmaColor= sigmac , sigmaSpace= sigmas)
        #

    elif mode == 'median':
        kernel_size = config.get('kernel_size', 5) if config else 5
        img_result = cv.medianBlur(image, kernel_size)

    elif mode == 'gauss':
        kernel_size = config.get('kernel_size', 5) if config else 5
        img_result = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)

    elif mode == 'averaging':
        kernel_size = config.get('kernel_size', 5) if config else 5
        # averaging
        img_result = cv.blur(image, size=(kernel_size, kernel_size))

    else:
        errors.append(f"Invalid mode {mode}, available ['bilateral', 'median', 'gauss', 'averaging']")

    if 'erode' in config:
        img_result = cv.erode(img_result, kernel = (3, 2))

    if len(errors) > 0:
        return {
            'errors': errors
        }

    return {
        'images': {
            'processed': img_result
        }
    }

def rotate(image: object, config: dict = None) -> dict:
    """ Rotates the image by a particular degree

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    mode = config.get('mode', "auto") if config else "auto"
    limit = config.get('limit', 10) if config else 10
    step = config.get('step', 1) if config else 1
    threshold = config.get('threshold', 100) if config else 100
    angle = config.get('angle', 1) if config else 1

    if mode.lower() == 'auto':
        angle = bestangle(img=image, limit=limit, step=step, thresh=threshold)

    img_rotate = image.copy()
    img_rotate = scipy_rotate(image.copy(), angle=angle)

    return {
        "images": {
            "processed": img_rotate
        },
        "data": {},
    }

def realign(image: object, config: dict = None) -> dict:
    """ Returns the image that produces the highest horizontal
    pixel count, the function will use a scoring function, the
    algorithm will aim to process the image, and return the
    measure that gives the highest score.

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function

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

def deskew(image: object, config: dict = None) -> dict:
    """ resizes the image based on a trapezoid and curve distortion will
    modify to produce a retangluar output.

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function

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

def skeleton(image: object, config: dict = None) -> dict:
    """ reduces the image to  single pixel line per line and object

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A dictionary of params for the function
        engine: str
            skimage, dilate, zhangsuen

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    engine = config.get('engine','fast') if config else 'fast'

    skeleton = skimage.morphology.skeletonize(image)

    return {
        "images": {
            "processed": skeleton
        },
        "data": {},
    }
