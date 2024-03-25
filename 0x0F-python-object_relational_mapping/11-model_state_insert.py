#!/usr/bin/python3
"""Adds state to the database
take 3 arguments: mysql username, mysql password, db name
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()
    print(obj.id)
