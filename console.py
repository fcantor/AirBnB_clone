#!/usr/bin/python3
"""
command interpreter
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models import classes, storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


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
        'Shows attributes of <class> <id>'
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
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes instance of <class> <id>'
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
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        'Prints all <class> instances or all instances'
        args = parse(arg)
        objects = storage.all()
        if not args:
            v_list = []
            for k,v in objects.items():
                v_list.append(str(objects[k]))
            if v_list:
                print(v_list)
        else:
            v_list = []
            for k,v in objects.items():
                if v.__class__.__name__ == args[0]:
                    v_list.append(str(objects[k]))
            if v_list:
                print(v_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates class attribute.\nSyntax: update <class name> <id>\
 <attribute name> "<attribute value>"'
        args = parse(arg)
        objects = storage.all()
        if not args or args is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
        elif len(args) < 3 or args[2] == "":
            print("** attribute name missing **")
        elif len(args) < 4 or args[3] == "":
            print("** value missing **")
        else:
            for k,v in objects.items():
                print("ARGS3 TYPE {}".format(type(args[3])))
                key = args[0] + "." + args[1]
                if k == key:
                    attr = args[3].split('"')
                    t = val_type(attr[1])
                    objects[key].__dict__[args[2]] = (t)(attr[1])
                    objects[key].updated_at = datetime.now()
                    storage.save()
                    return
            print("** no instance found **")

    def emptyline(self):
        pass

def val_type(val):
    try:
        int(val)
        return (int)
    except ValueError:
        pass
    try:
        float(val)
        return (float)
    except ValueError:
        return (str)


def parse(arg):
    return arg.split()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
