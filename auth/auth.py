from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from crud.user import get_user_by_username
from sqlalchemy.orm import Session
from db.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = "e4a95950f77467b6340821a712052ed652bd834f159aa9e7af07847ac6c160e2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    credential_exceptin = HTTPException(status_code=401, 
                                        detail="Couldn't validate credentials",
                                        headers={"WWW-Authenticate": "Bearer"})
    
    try:
        pay_load = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = pay_load.get("sub")
        if not username: raise credential_exceptin
    except JWTError: raise credential_exceptin

    user = get_user_by_username(username, db)
    if not user: raise credential_exceptin

    return user