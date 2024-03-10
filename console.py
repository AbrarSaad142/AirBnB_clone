#!/usr/bin/python3
""" HBNB Module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State, "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """empty shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name a"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dic = storage.all()
            if key not in obj_dic:
                print("** no instance found **")
            else:
                print(obj_dic[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dic = storage.all()
            if key not in obj_dic:
                print("** no instance found **")
            else:
                del obj_dic[key]
                storage.save()

    def do_all(self, arg):
        """: Prints all string representation of
        all instances based or not on the class name"""
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[key]) for key in obj_dict])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key])
                   for key in obj_dict if key.startswith(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating
        attribute (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dict = storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                obj = obj_dict[key]
                setattr(obj, args[2], args[3])
                obj.save()


if __name__ == "__main__":
    """infinite loop"""
    HBNBCommand().cmdloop()
