from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, index=True)
    email = Column(String)
    password = Column(String)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    is_available = Column(Boolean, default=True)
