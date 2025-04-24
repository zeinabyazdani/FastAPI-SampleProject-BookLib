from sqlalchemy.orm import Session
from db.models import User
from schemas import UserCreate
from db.hash import Hash


def create_user(request: UserCreate, db: Session):
    user = User(username = request.username, 
                email = request.email, 
                password = Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()


def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def update_user(user_id, request: UserCreate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = request.username
        user.email = request.email
        user.password = Hash.bcrypt(request.password)
        db.commit()
        db.refresh(user)
        return user
    return None