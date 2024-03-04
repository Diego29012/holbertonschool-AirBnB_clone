#!/usr/bin/python3
"""
Test for the class Place
"""
from models.place import Place
import unittest


def test_place(unittest.TestCase):
    """
    Class that testing the class Place
    """
    model = Place()

    def test(self):
        self.assertEqual(self.model.name, "")
