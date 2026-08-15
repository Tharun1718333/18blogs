from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Blog


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Blog).offset(skip).limit(limit).all()


def get_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()


def create_blog(db: Session, user_id: int, blog_date: datetime, content: str):
    blog = Blog(user_id=user_id, blog_date=blog_date, content=content)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def update_blog(db: Session, blog_id: int, payload: dict):
    blog = get_blog(db, blog_id)
    if not blog:
        return None

    for key, value in payload.items():
        if value is not None:
            setattr(blog, key, value)

    db.commit()
    db.refresh(blog)
    return blog


def delete_blog(db: Session, blog_id: int):
    blog = get_blog(db, blog_id)
    if not blog:
        return False

    db.delete(blog)
    db.commit()
    return True
