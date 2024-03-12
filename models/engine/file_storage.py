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
        odict = FileStorage.__objects
        objectdict = {obj: odict[obj].to_dict()
                      for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(FileStorage.__file_path) as file:
                objectdict = json.load(file)
                for o in objectdict.values():
                    name = o['__class__']
                    del o['__class__']
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            return
