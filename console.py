#!/usr/bin/python3
"""
A console.py program that contains the
entry point of the command interpreter.
"""
import cmd


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


if __name__ == '__main__':
    """prevents code execution when imported"""
    HBNBCommand().cmdloop()
