#!/usr/bin/python3
"""Test for the class User"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """User test cases"""


    def test_attr_init(self):
        """Test if attributes initialise as empty strings"""
        self.assertEqual(self.obj1.email, "")
        self.assertEqual(self.obj1.password, "")
        self.assertEqual(self.obj1.first_name, "")
        self.assertEqual(self.obj1.last_name, "")
