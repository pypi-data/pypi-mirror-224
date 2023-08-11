"""A test case for the path utils module"""
import logging
import glob
import os
import sys
import unittest

import numpy as np
import cv2 as cv

from lost_cat_images.utils import color_segmentation
from lost_cat_images.utils import denoise
from lost_cat_images.utils import realign
from lost_cat_images.utils import deskew
from lost_cat_images.utils.clean import skeleton
from lost_cat_images.utils.clean import rotate

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler(f"logs/test_clean.log")
logger.addHandler(file_handler)

class TestClean(unittest.TestCase):
    """A container class for the clean functions"""

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

    def test_skeleton(self):
        """will skeltonize and image"""
        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f)

            sk_data = skeleton(image=img)

            for label, img_res in sk_data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.SK.{label}.png', img_res)

    def test_color_segmentation(self):
        """Test the color segmentation"""

        config = {
            "ranges": [
                {"min":(20, 0, 200), "max":(80, 100, 255)}
            ]
        }

        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f,cv.IMREAD_UNCHANGED)
            logger.info("IMG: %s", img.shape)

            sg_data = color_segmentation(image=img, config=config)

            for label, img_res in sg_data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.CS.{label}.png', img_res)

    def test_color_segmentation_dict(self):
        """Test the color segmentation"""

        config = {
            "ranges": [
                {"min":{"h": 20,"s": 0,"v": 200}, "max":{"h": 80,"s": 100,"v": 255}}
            ]
        }

        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f,cv.IMREAD_UNCHANGED)
            logger.info("IMG: %s", img.shape)

            sg_data = color_segmentation(image=img, config=config)

            for label, img_res in sg_data.get("images",{}).items():
                logger.info('Saving image %s %s %s', name, fidx, label)
                cv.imwrite(f'data/{name}.{fidx}.CSD.{label}.png', img_res)

    def test_denoise(self):
        """Test the denoise function"""

        config_main = {
            "bilateral": {
                "mode": "bilateral",
                "diameter": 9,
                "sigmacolor": 75,
                "sigmaspace": 75,
            },
            "median": {
                "kernelsize": 5,
            },
            "gauss": {
                "kernelsize": 5,
            },
            "averaging": {
                "kernelsize": 5,
            }
        }

        for fidx, f in enumerate(self.files):
            if not f.lower().endswith('basic.png'):
                continue
            _, filename = os.path.split(f)
            name, _ = os.path.splitext(filename)

            logger.info("File[%s]: %s", fidx, f)
            img = cv.imread(f,cv.IMREAD_UNCHANGED)
            logger.info("IMG: %s", img.shape)

            for label, config in config_main.items():
                data = denoise(image=img, config=config)
                for img_label, img_res in data.get("images",{}).items():
                    logger.info('Saving image %s %s %s', name, fidx, label)
                    cv.imwrite(f'data/{name}.{fidx}.DN.{label}.{img_label}.png', img_res)
