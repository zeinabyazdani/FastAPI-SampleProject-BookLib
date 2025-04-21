from pydantic import BaseModel


class UserCreate(BaseModel):
    name:str
    email: str
    password: str


class UserOut(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
