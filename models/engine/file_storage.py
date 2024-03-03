#!/usr/bin/python3
"""
FileStorage
"""
import json
from models.base_model import BaseModel


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
        return FileStorage.__objects

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
        c_dictionary = {key: value.to_dict() for key, value in
                        FileStorage.__objects.items()}
        with open(filename, "w", encoding='UTF-8') as file:
            json.dump(c_dictionary, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                file_content = f.read()
                    for key, value in json.load(json_content).items():
                        FileStorage.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
