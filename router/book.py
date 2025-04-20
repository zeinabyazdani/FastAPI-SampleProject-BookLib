from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from crud import book


router = APIRouter(prefix="/books", tags=['book'])


@router.post('/')
def add_book_view(title:str, author:str, year:int, is_available:bool, db: Session = Depends(get_db)):
    return book.add_book(db, title, author, year, is_available)


@router.get('/')
def get_all_books_view(db: Session = Depends(get_db)):
    return book.get_books(db)


@router.get('/{book_id}')
def get_book_view(book_id, db: Session = Depends(get_db)):
    return book.get_book_by_id(db, book_id)


@router.put('/{book_id}')
def update_book_view(book_id:int, title:str, author:str, year:int, is_available:bool, db: Session = Depends(get_db)):
    return book.update_book(db, book_id, title, author, year, is_available)


@router.get('/available/')
def available_books_view(db: Session = Depends(get_db)):
    return book.available_books(db)


@router.get('/borrow/{book_id}')
def get_borrow_view(book_id, db: Session = Depends(get_db)):
    return book.get_borrow(db, book_id)


@router.get('/return/{book_id}')
def get_return_view(book_id, db: Session = Depends(get_db)):
    return book.get_return(db, book_id)


@router.delete('/{book_id}')
def delete_book_view(book_id, db: Session = Depends(get_db)):
    return book.delete_book(db, book_id)
