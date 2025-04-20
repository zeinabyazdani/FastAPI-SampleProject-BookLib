from db.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)
    email = Column(String)
    password = Column(String)

