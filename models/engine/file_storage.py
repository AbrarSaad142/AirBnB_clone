#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances:
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """that serializes instances to a JSON
    file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as jsonFile:
            json.dump(json_object, jsonFile)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as jsonFile:
                for key, value in json.load(jsonFile).items():
                    attribute_value = eval(value['__class__'])(**value)
                    self.__objects[key] = attribute_value
        except FileNotFoundError:
            pass
