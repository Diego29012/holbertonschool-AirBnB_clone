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
    def __init__(self, *args, **kwargs):
        """Initialises a new instance or sets attributes based on kwargs"""
        from . import storage
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.now()
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        STR method that return a str
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Method that update the instance attribute "update_at"
        """
        from . import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This function return a dictionary with all keys and values
        from __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['id'] = self.id
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
