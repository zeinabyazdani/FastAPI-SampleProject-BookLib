from sqlalchemy.orm import Session
from db.models import Borrow
from datetime import datetime


def create_borrow(book_id: int, user_id: int, db: Session):
    not_available = db.query(Borrow).filter(Borrow.book_id == book_id, 
                                            Borrow.return_date.is_(None)).first()
    if not_available: 
        return None
    
    new_borrow = Borrow(user_id=user_id, book_id=book_id)
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)

    return new_borrow


def return_book(book_id: int, user_id: int, db: Session):
    borrow = db.query(Borrow).filter(Borrow.book_id == book_id,
                                     Borrow.user_id == user_id,
                                     Borrow.return_date.is_(None)).first()
    if not borrow:
        return None
    
    borrow.return_date = datetime.utcnow()
    db.commit()
    db.refresh(borrow)

    return borrow


def user_borrow_list(user_id: int, db: Session):
    return db.query(Borrow).filter(Borrow.user_id == user_id).all()


def borrow_history(book_id: int, db: Session):
    return db.query(Borrow).filter(Borrow.book_id == book_id).all()
