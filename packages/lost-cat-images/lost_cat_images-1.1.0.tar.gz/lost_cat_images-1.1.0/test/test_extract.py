"""A test case for the path utils module"""
import logging
import glob
import os
import sys
import unittest

import cv2 as cv

from lost_cat_images.utils import extract_contours
from lost_cat_images.utils import boxes
from lost_cat_images.utils import analyze
from lost_cat_images.utils import text
from lost_cat_images.utils.extract import line

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler(f"logs/testextract.log")
logger.addHandler(file_handler)

class TestExtract(unittest.TestCase):
    """A container class for the extract functions"""

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

    def test_extract_contours(self):
        """will test the contours from a drawing"""
        ec_config = {

        }

        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, ext = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            if ext.lower() not in ['.png']:
                continue

            image = cv.imread(f)
            data = extract_contours(image=image, config=None)

            # check the right elements are created...
            self.assertIn('contours', data.get('data',{}), 'Missing contours')
            contours = data.get('data',{}).get('contours',[])

    def test_line(self):
        """will test line function"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, ext = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            if ext.lower() not in ['.png']:
                continue

            config = {
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
            }

            image = cv.imread(f)
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

            data = line(image=image, config=config)

            # check the right elements are created...
            self.assertIn('lines', data.get('data',{}), 'Missing lines')
            lines = data.get('data',{}).get('lines',[])
