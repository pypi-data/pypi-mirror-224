""""""
from datetime import datetime
import logging
import cv2 as cv
import numpy as np

from scipy.ndimage import interpolation

logger = logging.getLogger(__name__)

def convert_image(image: object, config: dict = None) -> dict:
    """ Converts an image from one format to another. uses opencv for the
    conversion protocol.

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
            source: str
                The type label of the source image
            dest: str
                The type label of the destination image

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    image = np.array(image).copy()

    source = config.get('source', 'bgr').lower() if config else 'bgr'
    dest = config.get('dest', 'rgb').lower() if config else 'rgb'

    mapping = {
        "bgr": {
            "gray": cv.COLOR_BGR2GRAY,
            "hsv": cv.COLOR_BGR2HSV,
            "rgb": cv.COLOR_BGR2RGB,
        },
        "rgb": {
            "bgr": cv.COLOR_RGB2BGR,
            "gray": cv.COLOR_RGB2GRAY,
            "hsv": cv.COLOR_RGB2HSV,
        },
        "hsv": {
            "bgr": cv.COLOR_HSV2BGR,
            "rgb": cv.COLOR_HSV2RGB,
        }
    }

    if cnvt := mapping.get(source,{}).get(dest):
        img_return = cv.cvtColor(image, cnvt)
        return {
            "images": {
                "processed": img_return
            }
        }
    else:
        return {
            "errors": f"Invalid Conversion {source} -> {dest}: allowed values ['bgr', 'rgb', 'gray', 'hsv']"
        }

def grayscale(image: object, config: dict = None) -> dict:
    """ This will convert an image to a gray scale image


    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
            source: str
                The type label of the source image

    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
        data: dict
            None
    """
    errors = []
    img_result = None

    image = np.array(image).copy()

    sourcetype = config.get('sourcetype', 'BGR') if config else 'BGR'
    if sourcetype.lower() == 'bgr':
        img_result = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    elif sourcetype.lower() == 'rgb':
        img_result = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    elif sourcetype.lower() == 'hsv':
        rgb = cv.cvtColor(image, cv.COLOR_HSV2RGB)
        img_result = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)

    else:
        errors.append(f"Invalid sourcetype {sourcetype}: available values ['bgr', 'rgb', 'hsv']")

    if len(errors) > 0:
        return {
            'errors': errors
        }

    return {
        'images': {
            'processed': img_result
        }
    }

def threshold(image: object, config: dict = None) -> dict:
    """ This will convert an image to a binary image using
    threshold parameters and also add erode

    Parameters
    ----------
    image: object
        Accepts an image object
    config: dict
        A doctionary of params for the function
            thres: double
                the lowest
            maxval: double

            type: int
                cv.THRESH_BINARY        : 0
                cv.THRESH_BINARY_INV    : 1
                cv.THRESH_TRUNC         : 2
                cv.THRESH_TOZERO        : 3
                cv.THRESH_TOZERO_INV    : 4
                cv.THRESH_MASK          : 7
                cv.THRESH_OTSU          : 8
                cv.THRESH_TRIANGLE      : 16
            erode: flag
                performs a (3,2) erode on the image
    Returns
    -------
    dict
        a dictionary with the following format
        images: dict
            processed: np.array
    """

    image = np.array(image).copy()

    thresh = config.get("thresh", 140) if config else 140
    maxval = config.get("maxval", 255) if config else 255
    thres_type = config.get("type", cv.THRESH_BINARY | cv.THRESH_OTSU) if config else cv.THRESH_BINARY | cv.THRESH_OTSU

    _, img_result = cv.threshold(src=image, thresh=thresh, maxval=maxval, type=thres_type)

    if 'erode' in config:
        kernel = np.ones((3,2), dtype=np.uint8)
        img_result = cv.erode(img_result, kernel, iterations=1)

    return {
        "images": {
            "processed": img_result
        }
    }
