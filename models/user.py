#!/usr/bin/python3
""" holds class User"""
from hashlib import md5
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = hashlib.md5(kwargs['password'].encode()
                                        ).hexdigest()
        elif 'password' in self.__dict__:
            self.password = hashlib.md5(self.password.encode()).hexdigest()

    def to_dict(self, save_to_disk=False):
        """Returns a dictionary containing user information"""
        user_dict = super().to_dict(save_to_disk)
        if not save_to_disk:
            user_dict.pop('password', None)
        return user_dict
