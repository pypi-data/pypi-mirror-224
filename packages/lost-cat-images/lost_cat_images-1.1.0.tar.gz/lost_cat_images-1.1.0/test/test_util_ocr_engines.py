"""A test case for the path utils module"""
import json
import logging
import unittest
import glob
import os
import cv2 as cv

from lost_cat_images.utils import NumpyArrayEncoder
from lost_cat_images.utils.utils_ocr_engines import ocr_azure, resize_image

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler("logs/test_utilsocrengine.log")
logger.addHandler(file_handler)

class TestUtilsOCREngines(unittest.TestCase):
    """A container class for the ocr engine module test cases"""

    @classmethod
    def setUpClass(cls):
        """ Set up for Trie Unit Tests..."""
        uri = os.path.join("data")
        if not os.path.exists(uri):
            os.makedirs(uri)
            logger.info("Creating %s", uri)
        cls.files = []

        uri = os.path.join(uri, "*")
        for f in glob.glob(uri):
            _, ext = os.path.splitext(f)
            if ext.lower() == ".png":
                cls.files.append(f)

    def test_ocr_azure(self):
        """test teh azure ocr run process"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)

            config = {
                'image': img.copy()
            }

            # call the
            data = ocr_azure(image=img, config=config)

            with open(f'data/{fidx}.{name}.azure.json', 'w') as fp:
                fp.write(json.dumps(data.get("data",{}), indent=4, cls=NumpyArrayEncoder))

            # save the images...
            for label, img_res in data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.OCR.AZ.{label}.png', img_res)

    def test_resize(self):
        """Test the resize fucntion"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)

            shape = img.shape
            y = shape[0]
            x = shape[1]

            maxx = int(x/2)
            maxy = int(y/2)

            img_small, ratio = resize_image(image=img, max_width=maxx, max_height=maxy)

            shape_small = img_small.shape

            self.assertLessEqual(shape_small[0], maxy, f'y size MaxY: {maxy} -> {shape_small[0]}')
            self.assertLessEqual(shape_small[1], maxx, f'x size MaxX: {maxx} -> {shape_small[1]}')
            self.assertLessEqual(ratio, 0.5, f'Incorrect Ratio {ratio} - Orig: {shape} Small: {shape_small}')
