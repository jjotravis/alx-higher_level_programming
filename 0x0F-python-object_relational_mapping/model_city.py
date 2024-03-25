#!/usr/bin/python3
"""class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, ForeignKey


Base = declarative_base()


class City(Base):
    """Inherits from Base
    id: primary, not null, auto increment
    name: string, 128 char"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
