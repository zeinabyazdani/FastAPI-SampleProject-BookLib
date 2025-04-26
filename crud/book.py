from sqlalchemy.orm import Session
from db.models import Book, Borrow
from schemas import BookCreate
from fastapi import HTTPException


def add_book(request: BookCreate, db: Session):
    book = Book(title = request.title, 
                author = request.author, 
                year = request.year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(book_id: int, db: Session):
    return db.query(Book).filter(Book.id==book_id).first()


def update_book(book_id, request: BookCreate, db: Session):
    book = db.query(Book).filter(Book.id==book_id).first()
    if book:
        book.title = request.title
        book.author = request.author
        book.year = request.year
        db.commit()
        db.refresh(book)
        return {"message": "Updated!"}
    return {"message": "Not found!"}


def available_books(db: Session):
    return db.query(Borrow).filter(Borrow.return_date.is_not(None)).all()
    return db.query(Book).join(Borrow).filter(Borrow.return_date.is_not(None)).all()


def delete_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id==book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False
