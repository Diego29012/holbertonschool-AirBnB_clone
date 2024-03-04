#!/usr/bin/python3
"""
Test for the class City
"""
from models.city import City
import unittest


def test_city(unittest.TestCase):
    """
    Class that testing the class City
    """
    model = City()

    def test(self):
        self.assertEqual(self.model.name, "")
