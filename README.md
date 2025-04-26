# FastAPI Library Project

A simple library management system built with **FastAPI**, using **SQLite** for storage and **Docker** for containerization.

---

## Features

- User management (create, update, delete users)
- Book management (create, update, delete books)
- Borrowing and returning books (with authentication)
- View loan history for users and books
- Input validation using **Pydantic schemas**
- Secure password hashing
- Proper error handling with **HTTPException**

---

## How to Run the Project

### 1. Build the Docker image

```bash
sudo docker build -t fastapi-library:v1 .
```

### 2. Run the Docker container

```bash
sudo docker run --rm -it --name fastapi-library-container -p 8000:8000 fastapi-library:v1
```

> After running, the FastAPI server will be available at:
> 
> [http://localhost:8000](http://localhost:8000)

---

## API Documentation

FastAPI automatically provides interactive API docs:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Project Structure

```
├── auth/
│   └── auth.py
├── crud/
│   └── user.py, book.py, borrow.py
├── db/
│   └── database.py, models.py, hash.py
├── router/
│   └── user.py, book.py, borrow.py, auth.py
├── schemas.py
├── main.py
├── requirements.txt
└── Dockerfile
```

---

## Authentication

- Users must **log in** to borrow or return books.
- Users can only **return books they have borrowed**.
- Borrow and return routes are **protected** with authentication.

---

## Requirements

If you want to run it without Docker:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

# Future Improvements

- Add Admin role for managing books and users
- Add due dates for borrowed books
- Improve error messages and validations
- Migrate database to PostgreSQL for production

---

> ## By Zeinab Yazdanin
