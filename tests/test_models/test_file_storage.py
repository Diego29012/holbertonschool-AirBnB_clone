#!/usr/bin/python3
"""
Test for file storage functions
"""
from models.engine.file_storage import FileStorage
import unittest

class test_file_storage(unittest.TestCase):
    """
    Class tahat testing file storage
    """
    file_storage = FileStorage

    def filename(self):
        """
        check __file_path
        """
        self.assertEqual(file_storage.__file_path, "file.json")

    def all(self):
        """
        check all function
        """
        self.assertEqual(file_storage.all(), "")

if __name__ == '__main__':
    unittest.main()