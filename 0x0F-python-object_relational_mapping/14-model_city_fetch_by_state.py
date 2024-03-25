#!/usr/bin/python3
"""Lists all state objects
take 3 arguments: mysql username, mysql password and database name
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for city, state in session.query(City, State)\
        .filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
