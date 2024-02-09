#!/usr/bin/python3
"""
AirBnB clone - The console
File_storage
"""

import json
from models.base_model import BaseModel


class Filestorage:
    """
    class sterializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}


