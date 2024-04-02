#!/usr/bin/python3
""" holds class Admin"""

from hashlib import md5
from sqlalchemy import create_engine, Column, String, Date, func
from base_model import BaseModel, Base
from flask_login import UserMixin

class Admin(BaseModel, Base, UserMixin):
    """Representation of a user """
    __tablename__ = 'admins'
    id = Column(String(60), primary_key=True, unique=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
