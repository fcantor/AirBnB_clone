#!/usr/bin/python3
"""
command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ description """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        'Quit command to exit the program'
        print('Peace out!')
        self.close()
        quit()
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == "__main__":
    HBNBCommand().cmdloop()
