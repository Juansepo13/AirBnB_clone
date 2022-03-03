#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import sys
import json
import cmd
import shlex
""" 6. Console 0.0.1 """

my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """-HBNBCommand(cmd.Cmd) is a class that inherits from cmd.Cmd
                    cmd.Cmd is methods to execute a command prompt command
                    line interface for a Python program.
       -prompt is a interpreter-specific string that is displayed to the user
       when they are ready to enter a command.
       -classes is a list of all the classes that inherit from BaseModel.
       -my_objects is a dictionary of all the instances of the classes
       in classes.
       -my_classes oa diccionary whit the classes.
       -storage is an instance of FileStorage.
       -self is an instance of HBNBCommand to use the methods of the class.
       -args is a list of arguments passed to the command.
       -args_list is a list of arguments passed to the command."""

    prompt = '(hbnb) '
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    """reload() reloads the JSON file

    instances = ["do_show", "do_destroy", "do_all", "do_update"]"""

    def do_quit(self, args):
        """Quit command to exit the program.\n"""
        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program"""
        quit()
        
 def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel \
saves it (to the JSON file) and prints the id.
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in my_classes:
            print("** class doesn't exist **")
            return
        if args[0] in my_classes:
            """if the args[0] is in my_classes, then the class exists"""
            new_object = eval(args[0])()
            new_object.save()
            """save() saves the changes in the JSON file"""
            print(new_object.id)
            """print the id of the object"""

    def do_show(self, args):
        """Prints the string representation of an instance, format:
        show <class name> <id>."""

        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
              shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if not args:
            print("** class name missing **")
            return
        elif args_list[0] not in my_classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        new_object = "{}.{}".format(args_list[0], args_list[1])
        """new_object is a string that is the class name an the id"""
        if new_object not in models.storage.all().keys():
            """if the new_object is not in the dictionary,
            then the object doesn't exist"""
            print("** no instance found **")
            return
        else:
            print("[{}] ({}) {}".format(args_list[0], new_object[1],
                  models.storage.all()[new_object]))
            """print the object in format [class name] (id) object"""
