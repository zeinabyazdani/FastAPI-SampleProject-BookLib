from sqlalchemy.orm import Session
from db.models import Book
from schemas.book import BookCreate
from fastapi import HTTPException


def add_book(db: Session, request: BookCreate):
    book = Book(title = request.title, 
                author = request.author, 
                year = request.year, 
                is_available = request.is_available)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id==book_id).first()


def update_book(book_id, db: Session, request: BookCreate):
    book = db.query(Book).filter(Book.id==book_id).first()
    if book:
        book.title = request.title
        book.author = request.author
        book.year = request.year
        book.is_available = request.is_available
        db.commit()
        db.refresh(book)
        return {"message": "Updated!"}
    return {"message": "Not found!"}



def available_books(db: Session):
    return db.query(Book).filter(Book.is_available.is_(True)).all()


def get_borrow(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book: raise HTTPException(status_code=404, detail="Book not found.")
    if not book.is_available: raise HTTPException(status_code=400, detail="Book is already borrowed.")
    book.is_available = False
    db.commit()
    db.refresh(book)
    return book


def get_return(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id==book_id).first()
    if not book: raise HTTPException(status_code=404, detail="Book not found.")
    if book.is_available: raise HTTPException(status_code=400, detail="Book is already returned.")

    book.is_available = True
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id==book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False
