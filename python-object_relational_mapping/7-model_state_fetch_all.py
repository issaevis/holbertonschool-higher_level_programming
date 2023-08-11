#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(u, p, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(Stare.id).all():
        print("{} {} {}".format(state.id, state.name))
    session.close()
