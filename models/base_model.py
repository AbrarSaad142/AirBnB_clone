#!/usr/bin/python3
"""model Base"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class declaration"""
    def __init__(self, *args, **kwargs):
        """constructor method"""
        if '__class__' in kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save method to save instance information in json file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method that return
        a dictionary containing all keys/values of __dict__ of the instance"""
        obj_formate = self.__dict__.copy()
        obj_formate['__class__'] = type(self).__name__
        obj_formate['created_at'] = self.created_at.isoformat()
        obj_formate['updated_at'] = self.updated_at.isoformat()
        return obj_formate

    def __str__(self):
        """__str__ method string represntation of the instance
        return
        [str] instance  """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
