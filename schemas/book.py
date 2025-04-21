from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    is_available: bool

    

class BookOut(BaseModel):
    title: str
    author : str
    year: int
    is_available: bool

    class Config:
        orm_mode = True    
    