"""A test case for the path utils module"""
import logging
import unittest
import glob
import os
import numpy as np
import cv2 as cv

from lost_cat_images.utils.image_templates import create_targets

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler("logs/test_utilstemplates.log")
logger.addHandler(file_handler)

class TestUtilsImageTemplates(unittest.TestCase):
    """A container class for the boxes module test cases"""

    def test_targets(self):
        """will test the default size and offsets"""
        targets, offsets = create_targets()

        self.assertIsInstance(targets, list, "Targets: Expeecting a list")
        self.assertIsInstance(offsets, list, "Offsets: Expeecting a list")

        for t in targets:
            self.assertIsInstance(t, np.ndarray, "Target: Expeecting a numpy array")
            x,y = t.shape
            self.assertEqual(x, 7, "X: Size is incorrect")
            self.assertEqual(y, 7, "Y: Size is incorrect")

    def test_newsize(self):
        """Will test the size parameter"""
        size = 7
        targets, offsets = create_targets(size=size)

        self.assertIsInstance(targets, list, "Targets: Expeecting a list")
        self.assertIsInstance(offsets, list, "Offsets: Expeecting a list")

        for t in targets:
            self.assertIsInstance(t, np.ndarray, "Target: Expeecting a numpy array")
            x,y = t.shape
            self.assertEqual(x, size, "X: Size is incorrect")
            self.assertEqual(y, size, "Y: Size is incorrect")
    