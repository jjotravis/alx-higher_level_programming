#!/usr/bin/python3
"""Lists all state objects with name passed
take 4 arguments: mysql username, mysql password, db name and state
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

    name = sys.argv[4]
    for state in session.query(State):
        if name == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
