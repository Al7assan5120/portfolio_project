#!/usr/bin/python3

from sqlalchemy import create_engine, Column, String, Date, func
from base_model import BaseModel, Base

class User(BaseModel, Base):
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True, unique=True)
    first_name = Column(String(128), primary_key=True)
    last_name = Column(String(128))
    email = Column(String(128))
    submitDate = Column(Date, default=func.current_date())
    availableDate = Column(Date)
    occupation = Column(String(128))
    status = Column(String(128), default="Pending")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

