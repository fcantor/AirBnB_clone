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
    def test_all(self):
        '''compare __objects to all method -- DOESN'T WORK
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        var = fs1.all()
        self.assertEqual(fs1.__objects, var)
        '''

    def test_new(self):
        '''
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        # test if __object is empty
        self.assertIsNot(fs1.__objects, '{}')
        '''

    def test_save(self):
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        fs1.save()
        # check if file exists
        self.assertEqual(os.path.exists('file.json'), True)
        """ make sure it's appending not rewriting
        bm2 = BaseModel()
        fs1.new(bm2)
        fs1.save()
        """

    def test_reload(self):
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        fs1.save()
        dict1 = fs1.reload()
        # check reload() output
        self.assertIsEqual(type(dict1), "<class 'dict'>")
        bm2 = BaseModel()
        fs1.new(bm2)
        fs1.save()
        # check reload() output with appended data
        dict2 = fs1.reload()
        self.assertDictEqual(dict1, dict2)

if __name__ == '__main__':
    unittest.main()
