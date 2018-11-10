#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
engine
"""

class FileStorage(BaseModel):
    """
    FileStorage
    """
    __file_path = "../../file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[k] = obj

    def save(self):
        with open(__file_path, mode='w') as f:
            f.write(json.dumps(__objects))

    def reload(self):
        with open(__objects) as f:
            return json.load(f)
