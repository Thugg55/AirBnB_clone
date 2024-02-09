#!/usr/bin/python3
"""
AirBnB clone - The console
File_storage module
"""

import json
from models.base_model import BaseModel


class Filestorage:
    """
    
    FileStorage - sterializes instances to a JSON file
                and deserializes JSON file to instances
    Args:
        __file_path: the path to store the objects
        __objects: a dict to store the objects
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns all the objects """
        return self.__objects

    def save(self, obj):
        """ saves the instance of an object to a file """
        with open(self.__file_path, "w+") as f:
            f.write()


