#!/usr/bin/python3

from sqlalchemy import create_engine, Column, String
from base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True, unique=True)
    first_name = Column(String(128), primary_key=True)
    last_name = Column(String(128))
    email = Column(String(128))
    date = Column(String(128))
    occupation = Column(String(128))

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

