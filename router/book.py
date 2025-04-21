from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from crud import book as db_book
from schemas.book import BookCreate, BookOut
from typing import List


router = APIRouter(prefix="/books", tags=['book'])


@router.post('/', response_model=BookOut)
def add_book_view(book: BookCreate, db: Session = Depends(get_db)):
    return db_book.add_book(db, book)


@router.get('/', response_model=List[BookOut])
def get_all_books_view(db: Session = Depends(get_db)):
    return db_book.get_books(db)


@router.get('/{book_id}', response_model=BookOut)
def get_book_view(book_id:int, db: Session = Depends(get_db)):
    book = db_book.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book

@router.put('/{book_id}')
def update_book_view(book_id:int, book: BookCreate, db: Session = Depends(get_db)):
    updated_book = db_book.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return updated_book


@router.get('/available/', response_model=List[BookOut])
def available_books_view(db: Session = Depends(get_db)):
    return db_book.available_books(db)


@router.get('/borrow/{book_id}')
def get_borrow_view(book_id: int, db: Session = Depends(get_db)):
    book = db_book.get_borrow(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book


@router.get('/return/{book_id}')
def get_return_view(book_id: int, db: Session = Depends(get_db)):
    book =  db_book.get_return(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return book


@router.delete('/{book_id}')
def delete_book_view(book_id: int, db: Session = Depends(get_db)):
    success = db_book.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found!")
    return {"message": "Successfully deleted!"}
