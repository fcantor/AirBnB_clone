#!/usr/bin/python3
""" Tests class Amenity """
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Tests different attributes and functionality of Amenity class """

    @classmethod
    def setup_class(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "spa"

    @classmethod
    def teardown_class(cls):
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

if __name__ == '__main__':
    unittest.main()
