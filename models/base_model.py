#!/usr/bin/python3
import cmd
from datetime import datetime
from uuid import uuid4
"""
module
"""

class BaseClass():
    """ Parent of all other classes """

    def __init__(self, id=None, created_at, updated_at):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at
