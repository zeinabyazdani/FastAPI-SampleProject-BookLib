from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from crud import borrow as db_borrow
from db.models import User
from auth.auth import get_current_user
from router.book import get_book_view
from schemas import BorrowOut
from typing import List


router = APIRouter(prefix="/borrow", tags=['borrow'])


@router.post('/{book_id}', response_model=BorrowOut)
def create_borrow(book_id: int, 
           db: Session=Depends(get_db),
           current_user: User=Depends(get_current_user)):
    
    book = get_book_view(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    new_borrow = db_borrow.create_borrow(book_id, current_user.id, db)
    if not new_borrow: 
        raise HTTPException(status_code=400, detail="The book is currently borrowed.")
    
    return new_borrow


@router.post('/return/{book_id}')
def return_book(book_id: int, 
                db:Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    
    returned = db_borrow.return_book(book_id, current_user.id, db)
    if not returned:
        raise HTTPException(status_code=400, detail="You have not borrowed this book.")
    
    return {"message": "Book returned successfully"}


@router.get('/', response_model=List[BorrowOut])
def user_borrow_list(db: Session = Depends(get_db), 
                     current_user: User = Depends(get_current_user)):
    return db_borrow.user_borrow_list(current_user.id, db)


@router.get('/history/{book_id}', response_model=List[BorrowOut])
def borrow_history(book_id: int, db: Session = Depends(get_db)):
    return db_borrow.borrow_history(book_id, db)
