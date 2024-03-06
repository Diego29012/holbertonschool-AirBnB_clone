# AirBnB clone - The console

## Table of Contents
1. [AirBnB Clone Project](#airbnb-clone-project)
2. [How to start it](#how-to-start-it)
3. [How to use it](#how-to-use-it)
4. [Project Requirements](#project-requirements)
5. [Testing](#testing)
6. [AUTHORS](#authors)
7. [File Descriptions](#file-descriptions)

## AirBnB Clone Project

This repository showcases a simplified AirBnB web application, offering a learning platform for fundamental web development, with a focus on backend aspects using Python.

### How to start it:

1. Navigate to the repository's root directory.
2. Execute the console.py file using Python: python3 console.py

### How to use it:

Once the command interpreter is running, use the following commands:
- `create`: Create a new object.
- `show`: Display an object based on its ID.
- `update`: Modify attributes of an object.
- `destroy`: Destroy an object.
- `all`: Display all objects.
- `quit`: Exit the command interpreter.


### Project Requirements:

- Python3 (version 3.8.5)

### Testing

All code adheres to unittest standards. Run the following command for tests: python3 -m unittest discover tests

### AUTHORS

This section provides a list of contributors to the repository. Refer to the AUTHORS file for a more detailed list at the repository's root.

- Diego Piñeyro <6237@holbertonstudents.com>
- Braian De León <6336@holbertonstudents.com>

## File Descriptions

|File|Description|
|---|---|
|[README.md](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/README.md)|General project information.|
|[AUTHORS](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/AUTHORS)|List of contributors.|
|[base_model.py](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) |the BaseModel class serving as a foundation for other models. Common methods like saving, converting to dictionary format, and generating unique IDs. |
|[__init__.py](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/models/engine/__init__.py)|Sets up the application's storage engine and loads previous data.|
|[file_storage.py](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)|FileStorage class for serialization/deserialization of instances in JSON format. Stores, retrieves, and saves objects.|
|[test_base_model.py](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py)|Rigorous tests for the BaseModel class.|
|[console.py](https://github.com/Diego29012/holbertonschool-AirBnB_clone/blob/main/console.py)|Entry point for the command interpreter.|
