#!/usr/bin/python3
""" ALX AirBnB Console """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        exit()

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is encountered."""
        print()
        exit()

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
