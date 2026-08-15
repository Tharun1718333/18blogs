from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)


def list_users_service(db: Session, skip: int = 0, limit: int = 100):
    return get_users(db, skip=skip, limit=limit)


def get_user_service(db: Session, user_id: int):
    return get_user(db, user_id)


def create_user_service(db: Session, gmail: str, username: str):
    return create_user(db, gmail=gmail, username=username)


def update_user_service(db: Session, user_id: int, payload: dict):
    return update_user(db, user_id, payload)


def delete_user_service(db: Session, user_id: int):
    return delete_user(db, user_id)
