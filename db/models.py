from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, index=True)
    email = Column(String)
    password = Column(String)

    borrows = relationship("Borrow", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

    borrows = relationship("Borrow", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrow"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("users.id"))
    user_id = Column(Integer, ForeignKey("books.id"))
    borrow_date = Column(DateTime, default=datetime.utcnow())
    return_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")

