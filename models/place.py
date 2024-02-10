#!/usr/bin/python3
""" Place module that defines the Place class """

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place - Defines the Place class that inherits from the BaseModel class
    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
    """
    name = ""
