from pydantic import BaseModel


class UserCreate(BaseModel):
    name:str
    email: str
    password: str


class UserOut(BaseModel):
    name: str
    email: str
