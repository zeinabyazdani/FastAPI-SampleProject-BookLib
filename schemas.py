from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    username:str
    email: str
    password: str


class UserOut(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    author: str
    year: int

    
class BookOut(BaseModel):
    title: str
    author : str
    year: int

    class Config:
        orm_mode = True    
    

class BorrowOut(BaseModel):
    book: BookOut
    borrow_date: datetime
    return_date: Optional[datetime]

    class Config:
        orm_mode = True
