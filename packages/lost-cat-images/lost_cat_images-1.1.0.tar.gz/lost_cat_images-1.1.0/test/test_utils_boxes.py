"""A test case for the path utils module"""
import logging
import unittest
import glob
import os
import numpy as np
import cv2 as cv

from lost_cat_images.utils.image_templates import create_targets
from lost_cat_images.utils.utils_boxes import find_targets, group_vertices, extract_shapes, process_box_contours, process_box_templates

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler("logs/test_utilsboxes.log")
logger.addHandler(file_handler)

class TestUtilsBoxes(unittest.TestCase):
    """A container class for the boxes module test cases"""

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

        # prep the targets
        cls.vertices = [(1,2),(2,3),(4,3),(1,4)]
        cls.targets, cls.offsets = create_targets(7)

    @classmethod
    def tearDownClass(cls):
        """ Tear down for Trie Unit Tests"""
        pass

    def test_process_templates(self):
        """will use the test images, to cehck for targets"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # binarize the image
            ret, img_thres = cv.threshold(img_gray,50,255,cv.THRESH_BINARY)
            logger.debug("Image: %s -> %s\n\t%s", img_thres.shape, type(img_thres), ret)

            # run the code
            config = {
                'threshold_border': 0.5,
                'image': img.copy(),
            }

            data = process_box_templates(image=img_thres, config=config)

            # save the images...
            for label, img_res in data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.PT.{label}.png', img_res)

    def test_process_contours(self):
        """will use the test images, to cehck for targets"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # binarize the image
            ret, img_thres = cv.threshold(img_gray,50,255,cv.THRESH_BINARY)
            logger.debug("Image: %s -> %s\n\t%s", img_thres.shape, type(img_thres), ret)

            config = {
                'threshold_border': 0.5,
                'border': 1,
                'image': img.copy(),
            }

            data = process_box_contours(image=img_thres, config=config)

            # save the images...
            for label, img_res in data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.PB.{label}.png', img_res)
