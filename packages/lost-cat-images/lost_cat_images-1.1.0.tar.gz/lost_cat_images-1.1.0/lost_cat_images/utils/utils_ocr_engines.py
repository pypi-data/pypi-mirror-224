import io
import json
import logging
import os
import time
import cv2 as cv
import numpy as np
import requests

from dotenv import load_dotenv
from PIL import Image
#from shapely import Polygon

logger = logging.getLogger(__name__)

# load in the env vars
load_dotenv()

def ocr_azure(image: object, config: dict = None) -> dict:
    """"""
    markup_image = config.get('image', None) if config else None
    max_dim = 10000
    data = {
        "images": {},
        "data": {},
    }
    img = image.copy()
    w, h, _ = img.shape[::-1]
    ratio = 1

    if w >= max_dim or h >= max_dim:
        img, ratio = resize_image(image=img, max_width=max_dim, max_height=max_dim)

    azure_json_object = get_text_azure(image=img, config=config)
    data['data']['ratio'] = ratio
    data['data']['raw'] = azure_json_object

    word_properties = get_word_properties_from_azure_json(azure_json_object, ratio=ratio)
    data['data']['texts'] = word_properties

    if markup_image is not None:
        ploylines = [word['boundingBox'] for d in word_properties for word in d['words']] # select all bounding boxes
        text_list = [word['text'] for d in word_properties for word in d['words']] # select all texts
        contours = np.array(ploylines, dtype=np.int32)
        cv.drawContours(image=markup_image, contours=contours, contourIdx=-1, color=(0,0,255), thickness=1) #  markup_image = draw_polygons(markup_image, contours, (0, 255, 0))

        for tidx, (text_val, contour) in enumerate(zip(text_list, contours)):
            M = cv.moments(contour)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.putText(markup_image, str(tidx), org= (cx,cy), fontScale=1, color=(255, 0, 0), thickness=1, fontFace=cv.FONT_HERSHEY_SIMPLEX)
            logger.debug("Idx: %s Text: %s Contour: %s ", tidx, text_val, contour)

        data['images']['markup'] = markup_image
        # data['data']['bbox'] = contours
        # data['data']['sep_text'] = text

    return data

def ocr_tesseract():
    """"""
    pass

def resize_image(image, max_width=4200, max_height=4200):
    image = np.array(image).copy()
    # Get the original width and height
    image = np.array(image).copy()
    shape = image.shape

    orig_width = shape[1]
    orig_height = shape[0]

    # If both max width and max height are given, use the smaller ratio
    if max_width and max_height:
        # Check if the original width or height is larger than the max size
        if orig_width > max_width or orig_height > max_height:
            width_ratio = max_width / orig_width
            height_ratio = max_height / orig_height
            ratio = min(width_ratio, height_ratio)
        else:
            # Return the original image if it is smaller than the max size
            return image, 1
    # If only max width is given, use the width ratio
    elif max_width:
        # Check if the original width is larger than the max width
        if orig_width > max_width:
            ratio = max_width / orig_width
        else:
            # Return the original image if it is smaller than the max width
            return image, 1
    # If only max height is given, use the height ratio
    elif max_height:
        # Check if the original height is larger than the max height
        if orig_height > max_height:
            ratio = max_height / orig_height
        else:
            # Return the original image if it is smaller than the max height
            return image, 1
    # If neither is given, return the original image
    else:
        return image, 1

    # Calculate the new width and height based on the ratio
    new_width = int(orig_width * ratio)
    new_height = int(orig_height * ratio)

    # Resize the image with the new dimensions
    resized_image = cv.resize(src=image, dsize=(new_width, new_height))
    logger.debug("Resize: R: %s W: %s H: %s => NW: %s NH: %s ", ratio, orig_width, orig_height, new_width, new_height)

    # Return the resized image
    return resized_image, 1/ratio

def draw_polygons(image, polygons, color=(0, 255, 0)):
    # Convert the PIL image to an OpenCV image using the numpy array interface
    image = np.array(image).copy()

    # Convert the color space from RGB to BGR since OpenCV uses BGR by default
    opencv_image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    # Loop through each Polygon object in the list
    for polygon in polygons:
        # Draw the polygon on the image using cv2.polylines
        cv.polylines(opencv_image, [polygon], True, color, 1)

    # Return the PIL image with the polygons drawn
    return opencv_image

def get_text_azure(image: object, config: dict = None) -> dict:
    """
    Get the OCR text throught Azure engine

    Parameters
    ------
    image: object
        Accepts an image object
    config: dict
        use_cache: bool
            To prevent from consuming credits again for the same image
            file when developing, set `use_cache` as True.
            Otherwise, if you want to use Azure to detect text again, set it as False.
    Return
    ------
        data: json

    """
    api_path = os.getenv("AZURE_COGNITIVE_API_PATH")
    subscription_key = os.getenv("AZURE_COGNITIVE_API_KEY")

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'content-type': 'application/octet-stream'
    }

    # save the image to a bytes.io buffer
    image_buffer = io.BytesIO()
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    image.save(image_buffer, format='PNG')
    binary_data = image_buffer.getvalue()

    response = requests.post(api_path, headers=headers, data=binary_data)
    if response.status_code == 200:
        return_object = response.json()
        return return_object
    elif response.status_code == 202:
        url = response.headers['Operation-Location']
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
        }
        return_object = requests.get(url, headers=headers).json()
        while 1:
            if 'status' in return_object and return_object['status'] == 'running':
                time.sleep(1)
                return_object = requests.get(url, headers=headers).json()
            else:
                return return_object
    else:
        # <TODO: create a raise error here to be captured>
        logging.error(f"Failed to get image converted to text. "
                      f"Error Details: {response.text} Error Code: {response.status_code}")

def get_word_properties_from_azure_json(json_object, ratio: float = 1.0):
    """
    Get the word properties from the azure json object
    It also calculate the height of the word box
    :param json_object:
    :return:
    """
    word_boxes = []
    for result in json_object['analyzeResult']['readResults']:
        for line in result['lines']:
            if 'boundingBox' in line and 'text' in line:
                if 'words' in line:
                    cluster_detail = {
                            "word_cluster":None,
                            "word_cluster_box":None,
                            "words":[]
                        }
                    cluster_detail['word_cluster'] = line['text']
                    cluster_detail['word_cluster_box'] = convert_to_xy_tuple(line['boundingBox'], ratio=ratio)
                    for word in line['words']:
                        if 'boundingBox' in word and 'text' in word:
                            logger.debug("WR: %s S: %s", ratio, word['boundingBox'])
                            word['boundingBox'] = convert_to_xy_tuple(word['boundingBox'], ratio=ratio)
                            logger.debug(" -> %s", cluster_detail['word_cluster_box'])
                            cluster_detail['words'].append(word)

                    logger.debug("CR: %s S: %s -> %s", ratio, line['boundingBox'], cluster_detail['word_cluster_box'])
                    word_boxes.append(cluster_detail)
    return word_boxes

def convert_to_contour(coordinates: list, ratio: float = 1.0) -> np.array:
    """
    parameters
    ----------
    coordinates: list
        [x, y, x1, y1, ..., xn, yn]
    returns
    -------
    contour: np.array
        [[x,y], [x1,y1], ..., [xn,yn]]
    """
    contour = []
    # Loop through the coordinates list with a step of 2
    for i in range(0, len(coordinates), 2):
        # Get the x and y values at the current index and the next index
        x = int(coordinates[i] * ratio)
        y = int(coordinates[i + 1] * ratio)

        # Create a [x,y] and append it to the contour
        contour.append([x, y])

    # Return the contour
    return contour

def convert_to_xy_tuple(coordinates, ratio: float = 1.0):
    """
    Convert the coordinates from the format [x, y, x, y, x, y, x, y] to [(x, y), (x, y), (x, y), (x, y)]
    :param coordinates:
    :return:
    """
    # Create an empty list to store the tuples
    tuples = []
    # Loop through the coordinates list with a step of 2
    for i in range(0, len(coordinates), 2):
        # Get the x and y values at the current index and the next index
        x = int(coordinates[i] * ratio)
        y = int(coordinates[i + 1] * ratio)
        # Create a tuple of (x,y) and append it to the tuples list
        tuples.append((x, y))
    # Return the tuples list
    return tuples

def get_polygon_height(polygon):
    """
    Get the height of the polygon
    :param polygon:
    :return:
    """
    # Get the minimum and maximum y coordinates of the polygon
    miny, maxy = polygon.bounds[1], polygon.bounds[3]
    # Calculate the height as the difference between the maximum and minimum y coordinates
    height = maxy - miny
    # Return the height
    return height

def get_azure_json_save_file_path(pdf_path):
    json_path = os.getenv("RAW_AZURE_JSON_FILE_PATH")
    filename = os.path.basename(pdf_path)
    filename = os.path.splitext(filename)[0]
    return os.path.join(json_path, f"{filename}.json")

def save_azure_json_to_file(json_object, pdf_path):
    """
    Save Raw Azure JSON file after running OCR
    :param json_object:
    :param pdf_path:
    :return:
    """
    json_path = os.getenv("RAW_AZURE_JSON_FILE_PATH")
    if not os.path.exists(json_path):
        os.makedirs("data/azure_raw_json")
    with open(get_azure_json_save_file_path(pdf_path), 'w') as fp:
        fp.write(json.dumps(json_object, indent=2))

def get_tesseract_json_save_file_path(pdf_path):
    json_path = os.getenv("RAW_TESSERACT_JSON_FILE_PATH")
    if json_path == None or not os.path.exists(json_path):
        if not os.path.exists("data/tesseract_raw_json"):
            os.makedirs("data/tesseract_raw_json")
        json_path = os.path.join(os.getcwd(), "data/tesseract_raw_json")
    filename = os.path.basename(pdf_path)
    filename = os.path.splitext(filename)[0]
    return os.path.join(json_path, f"{filename}.json")

def save_tesseract_json_to_file(json_object, pdf_path):
    """
    Save Raw tesseract JSON file after running OCR
    :param json_object:
    :param pdf_path:
    :return:
    """
    json_path = os.getenv("RAW_TESSERACT_JSON_FILE_PATH")
    if json_path == None or not os.path.exists(json_path):
        if not os.path.exists("data/tesseract_raw_json"):
            os.makedirs("data/tesseract_raw_json")
        json_path = os.path.join(os.getcwd(), "data/tesseract_raw_json")
    with open(get_tesseract_json_save_file_path(pdf_path), 'w') as fp:
        fp.write(json.dumps(json_object, indent=2))


def xywh_to_xyxy(x, y, w, h):
    """
    Convert the coordinates from the format [x, y, w, h] to [x1, y1, x2, y2, x3, y3, x4, y4]
    :param x:
    :param y:
    :param w:
    :param h:
    :return:
    """
    # Calculate the bottom-right corner coordinates
    x2 = x + w
    y2 = y + h
    # Return a tuple of four corner coordinates
    return (x, y), (x2, y), (x2, y2), (x, y2)

def get_text_tesseract(
    image: object,
    config: dict = None,
    pdf_path: str = None,
    save_json: bool = True,
    ):
    import pytesseract
    # import pandas as pd
    # set up tesseract environmental PATH
    pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")
    def_opt = "--psm 1"
    tess_options = config.get("tesseract", {}).get("i2d", def_opt) if config else def_opt

    json_path = os.getenv("RAW_TESSERACT_JSON_FILE_PATH")
    if json_path == None or not os.path.exists(json_path):
        if not os.path.exists("data/tesseract_raw_json"):
            os.makedirs("data/tesseract_raw_json")
        json_path = os.path.join(os.getcwd(), "data/tesseract_raw_json")
    if pdf_path is None:
        logging.error("PDF path cannot be None.")
        raise ValueError("PDF path cannot be None.")
    filename = os.path.basename(pdf_path)
    filename = os.path.splitext(filename)[0]
    tesseract_save_file_path = os.path.join(json_path, f"{filename}.json")

    # extract data
    d = pytesseract.image_to_data(image=image, output_type=pytesseract.Output.DICT, config=tess_options)
    if save_json:
        save_tesseract_json_to_file(d, tesseract_save_file_path)
    return d
