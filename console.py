#!/usr/bin/python3
"""
command interpreter
"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """ command-line interpreter class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()

    def do_EOF(self, arg):
        'EOF command to exit the program'
        quit()

    def do_create(self, arg):
        'Creates new instance'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in type(self).classes:
            print("** class doesn't exist **")
        else:
            obj = type(self).classes[args[0]]()
            obj.save
            print(obj.id)

    def do_show(self, arg):
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in type(self).classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k,v in objects.items():

        print("** no instance found **")

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass

    def emptyline(self):
        pass



def parse(arg):
    return arg.split()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
