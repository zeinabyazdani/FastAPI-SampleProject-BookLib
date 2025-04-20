from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create engine: connect us to database
engine = create_engine("sqlite:///./booklib.db", connect_args={'check_same_thread': False})

# Class for create session: connection with database
Sessionlocal = sessionmaker(bind=engine)

# Class for create a table in database
Base = declarative_base()


def get_db():
    session = Sessionlocal()
    try:
        yield session
    finally:
        session.close()
