from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    email: str
    password: str


class UserOut(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
