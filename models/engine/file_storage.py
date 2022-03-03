#!/usr/bin/env python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path



class FileStorage:
    """ Class FileStorage that serilizes
    and deserialize instances to JSON
        __file_path: the path of the json file
        __objects: a dictionnary of all objects"
    """
    def __init__(self):
        """ initializes FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
           dicttionary: an empty dictionnary
           Open the dictionary in write mode
           dump the dictionary in the file f
        """
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, f)
