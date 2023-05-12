#!/usr/bin/python3
"""  This program contains the entry point of the command interpreter
"""

import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    """ hbnb command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(seif, arg):
        """ A method that will exit the program """
        return True

    def emptyline(self):
        """ This method does nothing when an empty line is entered """
        pass

    def help(self):
        """ This methods provide help messages for the commands """
        prints("")

    def do_create(self, arg):
        """ Creates a new instance BaseModel """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            arg = arg.split()
            new_instance = eval(arg[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints string representation of an instance """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return

        arg = arg.split()
        instance_key = arg[0] + "." + arg[1]

        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()

        try:
            str_rep = all_objs[instance_key]
            print(str_rep)
        except KeyError:
            print("** no instance found **")

    def do_destory(self, arg):
        """ Deletes an instance based on the class name and id
            save the change into the JSON file
        """
        if len(arg) == 1:
            print("** instance id missing **")
            return

        arg = arg.spilt()
        intance_key = arg[0] + "." + arg[1]

        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()

        try:
            del all_obj[instance_key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, arg):
        """ Print string representation of all instances based
            or not on the class name
        """
        new_list = []
        new_list2 = []
        storage = FileStorage()
        storage.reload()
        all_objs = storage.all()

        for key, value in all_obj.item():
            new_list.append(value.__str__())
        print(new_list2)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file)
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return


if __name__ == '__main__':
    """ prevents running on imort"""
    HBNBCommand().cmdloop()
