#!/usr/bin/python3
""" ALX AirBnB Console """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is encountered."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
