#!/usr/bin/python3
""" init file """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

classes = {'BaseModel': BaseModel,
    'User': User}

storage = FileStorage()
storage.reload()
