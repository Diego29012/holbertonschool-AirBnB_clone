#!/usr/bin/python3
"""
Test for the clase amenity
"""
from models.amenity import Amenity
import unittest


def test_amenity(unittest.TestCase):
    """
    Class that testing the clas amenity
    """
    model = Amenity()

    def test(self):
        self.assertEqual(self.model.name, "")
