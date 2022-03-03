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
