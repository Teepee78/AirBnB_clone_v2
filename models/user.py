#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import String, Column, ForeignKey
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        'Place', cascade='all, delete-orphan', backref='user')
    review = relationship('Review', backref='user',
                          cascade='all, delete-orphan')
