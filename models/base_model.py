#!/usr/bin/python3
"""
BaseModel class for AirBnB from datetime import datetime
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Create a new instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        STR method that return a str
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Method that update the instance attribute "update_at"
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This function return a dictionary with all keys and values
        from __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict
