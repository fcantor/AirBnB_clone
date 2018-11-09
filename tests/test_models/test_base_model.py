#!/usr/bin/python3
import unittest
from models.base_model import BaseClass
"""
Unittesting for base_model
"""

class TestBaseClass(unittest.TestCase):
    """
    instance id's should not be equal to one another

    """
    def test_id(self):
        bm1 = BaseClass()
        bm2 = BaseClass()
        self.assertIsInstance(bm1, BaseClass)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2, BaseClass)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertIsInstance(bm2.id, str)

    def test_created_updated(self):
        bm1 = BaseClass()
        bm2 = BaseClass()
        self.assertEqual("created_at", "updated_at")
        print(self.created_at)
        print(self.updated_at)

if __name__ == '__main__':
    unittest.main()
