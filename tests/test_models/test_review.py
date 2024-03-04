#!/usr/bin/python3
"""
Test for the clase Review
"""
from models.review import Review
import unittest


def test_amenity(unittest.TestCase):
    """
    Class that testing the clas Review
    """
    model = Review()

    def test(self):
        self.assertEqual(self.model.name, "")
