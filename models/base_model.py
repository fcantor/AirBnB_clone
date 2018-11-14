#!/usr/bin/python3
from datetime import datetime
import models
from uuid import uuid4
"""
module
"""


class BaseModel():
    """ Parent of all other classes """
    def __init__(self, *args, **kwargs):
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.strptime(
                        kwargs['created_at'], format)
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'], format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Returns a formatted string of class attributes """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ Updates updated_at value to current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Creates a dictionary of class attributes """
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
