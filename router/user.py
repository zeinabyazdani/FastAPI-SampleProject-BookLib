from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from crud import user as db_user
from schemas.user import UserCreate, UserOut
from typing import List


router = APIRouter(prefix='/user', tags=['user'])


# Create user
@router.post('/', response_model=UserOut)
def create_user_view(user: UserCreate, db: Session = Depends(get_db)):
    return db_user.create_user(db, user)


# Get users
@router.get('/', response_model=List[UserOut])
def get_all_users_view(db: Session = Depends(get_db)):
    return db_user.get_users(db)


# get user
@router.get('/{user_id}', response_model=UserOut)
def get_user_view(user_id: int, db: Session = Depends(get_db)):
    user = db_user.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user


# Delete user
@router.delete('/{user_id}')
def delete_user_view(user_id: int, db: Session = Depends(get_db)):
    success = db_user.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found!")
    return {"message": "Successfully deleted!"}


# Update user
@router.put('/{user_id}')
def update_user_view(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = db_user.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found!")
    return updated_user
