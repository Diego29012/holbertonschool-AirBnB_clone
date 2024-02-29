#!/usr/bin/python3
"""
FileStorage
"""
import json


class FileStorage():
    """
    That serializes instances to a JSON file and deserializes 
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """
        o_class = obj.__class__.__name__
        FileStorage.__objects[f"{o_class}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        filename = FileStorage.__file_path
        c_dictionary = {key: value for key, value in FileStorage.__objects.items()}
        with open(filename, "w", encoding='UTF-8') as file:
            json.dump(c_dictionary, file)

    def reload():
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
