from fastapi import FastAPI
from router import user, book, auth
from db import models
from db.database import engine


def init_routers(app: FastAPI) -> None:
    app.include_router(user.router)
    app.include_router(book.router)
    app.include_router(auth.router)


def create_app() -> FastAPI:
    app = FastAPI(title="Book Library Project")
    init_routers(app)
    return app


# Initialize database
models.Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = create_app()
