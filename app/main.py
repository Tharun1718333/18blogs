from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routers.blogs import router as blogs_router
from app.routers.events import router as events_router
from app.routers.todos import router as todos_router
from app.routers.users import router as users_router

app = FastAPI(title="18 Blogs API")

app.include_router(users_router)
app.include_router(todos_router)
app.include_router(blogs_router)
app.include_router(events_router)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}
