#!/usr/bin/python3
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""
Unittesting for file_storage
"""

class TestFileStorage(unittest.TestCase):
    """
    Testing methods within FileStorage class
    """
    def test_save(self):
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        fs1.save()
        # check if file exists
        self.assertEqual(os.path.exists('file.json'), True)
        # make sure it's appending not rewriting

if __name__ == '__main__':
    unittest.main()
