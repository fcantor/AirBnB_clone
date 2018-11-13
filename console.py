#!/usr/bin/python3
"""
command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import classes, storage

class HBNBCommand(cmd.Cmd):
    """ command-line interpreter class """
    prompt = '(hbnb) '

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
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        args = parse(arg)
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(key)
                print(storage.all()[key])

#        print("** no instance found **")

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