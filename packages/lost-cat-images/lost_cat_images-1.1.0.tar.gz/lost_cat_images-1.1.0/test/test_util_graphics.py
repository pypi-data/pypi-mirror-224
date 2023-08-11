"""A test case for the path utils module"""
import json
import logging
import unittest
import glob
import os
import cv2 as cv
import numpy as np

from lost_cat_images.utils.utils_graphics import angle_diff

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler("logs/test_utilsgraphics.log")
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

    def test_angle_diff(self):
        """test the angle_diff function"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)

            line1 = np.array([10,10,20,20], dtype = np.int32)
            line2 = np.array([20,20,10,10], dtype = np.int32)

            angle_Diff = angle_diff(line1, line2)
            self.assertAlmostEqual(180, angle_Diff, places= 0)
