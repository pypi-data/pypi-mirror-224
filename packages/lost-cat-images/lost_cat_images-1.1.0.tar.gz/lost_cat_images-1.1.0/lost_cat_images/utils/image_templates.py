"""This module contains a set of templates for box and shape detection"""
import logging
import cv2 as cv
import numpy as np

logger = logging.getLogger(__name__)

def create_targets(size: int = 7, bleed: int = 2) -> list:
    """Return a list of kernels useful for box corner
    detection.
    Generates an array and the offset coordinates

                1 ┎                         ┐ 2
        bleed       0  , 0  , 0  , 0  , 0  
                    0  , 255, 255, 255, 255
                    0  , 255, 255, 255, 255
                    0  , 255, 255, 255, 255
                    0  , 255, 255, 255, 255
                4 └                         ┘ 3
        offset  1: (0   , 0   )
                2: (0   , size)
                3: (size, size)
                4: (size, 0   )

    paramters
    ---------
    size: int default 5
        The szie of the target array
    bleed: int default 1
        The zero border widtrh for the target
    """
    targets:list = []
    offsets:list = []

    # create the base array...
    base_255 = np.full((size-bleed, size-bleed), 255, dtype=np.uint8)
    base_zeros = np.full((size, size), 0, dtype=np.uint8)
    base_rows = np.array(base_zeros[:bleed,:])

    top_left = np.c_[np.zeros((size-bleed,bleed)), base_255]
    top_left = np.r_[base_rows, top_left]
    targets.append(np.asarray(a=top_left,  dtype=np.uint8))
    offsets.append((0,0))

    top_right = np.c_[base_255, np.zeros((size-bleed,bleed))]
    top_right = np.r_[base_rows, top_right]
    targets.append(np.asarray(a=top_right,  dtype=np.uint8))
    offsets.append((size,0))

    bottom_right = np.c_[base_255, np.zeros((size-bleed,bleed))]
    bottom_right = np.r_[bottom_right, base_rows]
    targets.append(np.asarray(a=bottom_right,  dtype=np.uint8))
    offsets.append((size,size))

    bottom_left = np.c_[np.zeros((size-bleed,bleed)), base_255]
    bottom_left = np.r_[bottom_left, base_rows]
    targets.append(np.asarray(a=bottom_left,  dtype=np.uint8))
    offsets.append((size,size))

    return (targets, offsets)

# extension-pkg-allow-list
def process_image(image: object, targets: list, threshold: float = 0.8) -> dict:
    """Will process the image and use a variety of step to 
    get information from the image.


    parameters
    ----------
    image: object
        The source image, should be thresholded
    targets: list
        The targets to look for
    threshold: float
        The threshold value for a hit, default looks for 80% match
    
    returns
    -------
    dict:
        images
            processed
        data
            points
            x
            y
    """
    img_return = image.copy()
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_return, image_thres = cv.threshold(image_gray,75,255,cv.THRESH_BINARY)
    
    colors = [(0,0,255),(255,0,0),(0,255,0),(0,255,255)]

    x_points = {}
    x_values = set()
    y_points = {}
    y_values = set()

    for idx, target in enumerate(targets):
        logger.info("first target: %s", target)
        w, h = target.shape[::-1]
        res = cv.matchTemplate(image_thres,target,cv.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            #logger.info("Point: %s -> %s", pt,idx)
            x,y = pt
            cv.rectangle(image_return, pt, (x + w, y + h), colors[idx], 2)

            if x not in x_points:
                x_points[x] = {}
            if y not in x_points.get(x):
                x_points[x][y] = []
            x_points[x][y].append(idx)
            x_values.add(x)
            
            if y not in y_points:
                y_points[y] = {}
            if x not in y_points.get(y):
                y_points[y][x] = []
            y_points[y][x].append(idx)            
            y_values.add(y)
        
        cv.imwrite('res.png',image_return)

    # sort the points to help...
    x_sort = {}
    for x in sorted(x_points.keys()):
        x_sort[x] = {}
        for y in sorted(x_points.get(x,{}).keys()):
            x_sort[x][y] = x_points.get(x,{}).get(y,[])

    y_sort = {}
    for y in sorted(y_points.keys()):
        y_sort[y] = {}
        for x in sorted(y_points.get(y,{}).keys()):
            y_sort[y][x] = y_points.get(y,{}).get(x,[])
    
    # output the points
    logger.info("X:\n%s", x_sort)
    logger.info("Y:\n%s", y_sort)

    # find the complete rectangles....
    x_order = [[0,2],[1,3]]
    y_order = [[0,1],[2,3]]

    # get the vertical lines...

    # return the data
    return {
        "images": {
            "gray": image_gray,
            "thres": image_thres,
            "markup": image_return,
        },
        "data": {
            "points": {
                "x": x_points,
                "y": y_points,
            },
            "x": sorted(x_sort),
            "y": sorted(y_sort),
        }
    }
