import logging

from sqlalchemy import create_engine

from sqlalchemy import Column
from sqlalchemy import Integer

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StateCounter(Base):
    __tablename__ = "state_counter"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)

    def __repr__(self):
        return f'{self.count}'

    def get_base(self):
        return self.Base


def init_state_db(db_path):
    """
    Initialize the database.
    
    :param db_path: The url path to the database.
    :type db_path: str
    """
    try:
        engine = create_engine(db_path)
        Base.metadata.create_all(engine)

    except Exception as e:
        logging.error(e)

    else:
        print("Database started!")
        return engine

def increment_state_counter(engine, count):
    """
    Increment the state counter.
    
    args:
        engine: The url path to the database.
        count: The number of times the state was visited.
        return: void
    """
    delete_counter(engine)
    with Session(engine) as session:
        state_counter = StateCounter(count=count)
        if state_counter:
            session.add(state_counter)
            session.commit()

def delete_counter(engine):
    """
    Delete the state counter.
    
    args:
        engine: The url path to the database.
        return: void
    """
    try:
        with Session(engine) as session:
            session.query(StateCounter).delete()
            session.commit()
    
    except Exception as e:
        logging.error(e)
        return

def get_counter(engine):
    """
    Get the state counter.
    
    args:
        engine: The url path to the database.
        return: The current counter value.
    """
    with Session(engine) as session:
        counter = session.query(StateCounter).order_by(StateCounter.count.desc()).first()

    return str(counter)
