#!/usr/bin/python3
"""
Is the Module for the command interpreter.
"""

import cmd
import json
import models

class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class definition for the command interpreter.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if args and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        if args:
            objects = {key: obj for key, obj in objects.items() if args[0] in key}
        print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = models.storage.all()[key]
        if hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            try:
                if attribute_type == int:
                    attribute_value = int(attribute_value)
                elif attribute_type == float:
                    attribute_value = float(attribute_value)
            except ValueError:
                pass
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
