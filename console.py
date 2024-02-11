#!/usr/bin/python3
"""
A console.py program that contains the
entry point of the command interpreter.
"""
import cmd
import re
from datetime import datetime
import models

class HBNBCommand(cmd.Cmd):
    """cmd console class """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        End of file. Exits the console.
        """
        print("")
        return True

    def do_quit(self, line):
        """
        quit(exits) the program
        """
        return True

    def emptyline(self):
        """
        don't do anything for an
        empty line 
        """
        pass


    def do_create(self, line):
        """
        creates a new instance of Basemodel,
        saves it and prints the id

        method breaks a string of arguments down
        into smaller chunks.

        If the class name is missing, print 
        "** class name missing **"
        """
         if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[line]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance - class name and id

        This method splits the arguments into smaller strings before the
        arguments are used. 

        If the class name is missing, "** class name missing **" will be
        printed to the screen. If the class name doesn't exist, "** class
        doesn't exist **" will be printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

