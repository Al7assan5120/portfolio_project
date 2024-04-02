#!/usr/bin/python3

import model
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from model.user import User
from model.admin import Admin
from base_model import Base

db_url = "mysql://porto:123456@localhost/applicants"
classes = {"User" : User, "Admin" : Admin}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(db_url)

    def reload(self):
        """query on the current database session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
            """call remove() method on the private session attribute"""
            self.__session.remove()

    def all(self, cls):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = model.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(model.storage.all(clas).values())
        else:
            count = len(model.storage.all(cls).values())

        return count

    # def get(self, id):
    #     """
    #     Returns the object based on the class name and its ID, or
    #     None if not found
    #     """

    #     all_cls = model.storage.all()
    #     for value in all_cls.values():
    #         if (value.id == id):
    #             return value
    #     return "None"
