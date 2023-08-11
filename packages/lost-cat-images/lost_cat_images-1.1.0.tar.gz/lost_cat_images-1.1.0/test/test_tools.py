"""A test case for the path utils module"""
import logging
import glob
import os
import sys
import unittest

from lost_cat_images.utils import convert_image
from lost_cat_images.utils import grayscale
from lost_cat_images.utils import threshold
from lost_cat_images.utils.clean import denoise

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler(f"logs/test_tools.log")
logger.addHandler(file_handler)

class TestTools(unittest.TestCase):
    """A container class for the tools module"""

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
