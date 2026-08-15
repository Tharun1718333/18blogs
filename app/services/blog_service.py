from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.blog_repository import (
    create_blog,
    delete_blog,
    get_blog,
    get_blogs,
    update_blog,
)


def list_blogs_service(db: Session, skip: int = 0, limit: int = 100):
    return get_blogs(db, skip=skip, limit=limit)


def get_blog_service(db: Session, blog_id: int):
    return get_blog(db, blog_id)


def create_blog_service(db: Session, user_id: int, blog_date: datetime, content: str):
    return create_blog(db, user_id=user_id, blog_date=blog_date, content=content)


def update_blog_service(db: Session, blog_id: int, payload: dict):
    return update_blog(db, blog_id, payload)


def delete_blog_service(db: Session, blog_id: int):
    return delete_blog(db, blog_id)
