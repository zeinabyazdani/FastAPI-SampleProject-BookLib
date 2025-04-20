from fastapi import APIRouter
from db.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from crud import user


router = APIRouter(prefix='/user', tags=['user'])


# Create user
@router.post('/')
def create_user_view(name, email, password, db: Session = Depends(get_db)):
    return user.create_user(db, name=name, email=email, password=password)


# Get users
@router.get('/')
def get_all_users_view(db: Session = Depends(get_db)):
    return user.get_users(db)


# get user
@router.get('/{user_id}')
def get_user_view(user_id, db: Session = Depends(get_db)):
    return user.get_user_by_id(db, user_id=user_id)


# Delete user
@router.delete('/{user_id}')
def delete_user_view(user_id, db: Session = Depends(get_db)):
    return user.delete_user(db, user_id)


# Update user
@router.put('/{user_id}')
def update_user_view(user_id, name, email, password, db: Session = Depends(get_db)):
    return user.update_user(db, user_id, name, email, password)
