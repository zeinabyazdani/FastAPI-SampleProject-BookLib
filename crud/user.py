from sqlalchemy.orm import Session
from db.models import User
from schemas.user import UserCreate
from db.hash import Hash


def create_user(db: Session, request: UserCreate):
    user = User(name = request.name, 
                email = request.email, 
                password = Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def update_user(user_id, db: Session, request: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = request.name
        user.email = request.email
        user.password = Hash.bcrypt(request.password)
        db.commit()
        db.refresh(user)
        return user
    return None