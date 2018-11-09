#!/usr/bin/python3
import cmd
from datetime import datetime
from uuid import uuid4
"""
module
"""

class BaseClass():
    """ Parent of all other classes """

    def __init__(self, created_at=None, updated_at=None, id=None):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
