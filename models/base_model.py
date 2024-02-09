#!/usr/bin/python3
""" base model class """
import uuid
from datetime import datetime


class BaseModel:
    """
        BaseModel - defines all common attributes/methods for other classes
        Args:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime
                        when an instance is created
            updated_at: datetime - assign with the current datetime
                        when an instance is created and it will be updated
                        every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """ initialises the BaseModel class parameters """
        if args:
            pass
        elif kwargs:
            pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """ function to save the object instance """
         self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ converts the object attributes to dictionary """
        obj_dict = {}
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.strftime(date_format)
        obj_dict["updated_at"] = self.updated_at.strftime(date_format)
        obj_dict.update(self.__dict__)
        return obj_dict

    def __str__(self):
        """ returns the dict representation of the class """
        return "[{}] ({}) {}".format(self._class_._name, self.id, self.__dict__)
