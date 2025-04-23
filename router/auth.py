from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from crud.user import get_user_by_username
from db.hash import Hash
from datetime import timedelta
from auth.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(request.username, db)
    if not user: 
        raise HTTPException(status_code=404, detail="User not found")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(data={"sub": request.username}, 
                                       expires_delta= access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

