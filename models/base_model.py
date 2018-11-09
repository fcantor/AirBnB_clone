#!/usr/bin/python3
import cmd
from datetime import datetime
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
                    self.created_at = datetime.strptime(kwargs['created_at'], format)
            if 'updated_at' in kwargs.keys():
                    self.updated_at = datetime.strptime(kwargs['updated_at'], format)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
 
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        d = {}
        for k,v in self.__dict__.items():
            if v is not None:
                d[k] = v
        d['__class__'] = self.__class__.__name__

        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
