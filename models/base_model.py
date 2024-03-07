#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

"""Define BaseModel class"""

class BaseModel:
    """class declaration"""
    def __init__(self):
        """constructor method"""
  
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """save method to save instance information in json file"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict method that
        return 
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
