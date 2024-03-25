#!/usr/bin/python3
"""class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, create_engine


Base = declarative_base()


class State(Base):
    """Inherits from Base
    id: primary, not null, auto increment
    name: string, 128 char"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
