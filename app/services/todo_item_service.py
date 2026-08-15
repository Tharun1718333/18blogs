from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.todo_item_repository import (
    create_todo_item,
    delete_todo_item,
    get_todo_item,
    get_todo_items,
    update_todo_item,
)


def list_todo_items_service(db: Session, skip: int = 0, limit: int = 100):
    return get_todo_items(db, skip=skip, limit=limit)


def get_todo_item_service(db: Session, todo_id: int):
    return get_todo_item(db, todo_id)


def create_todo_item_service(
    db: Session,
    user_id: int,
    title: str,
    description: str | None = None,
    complete_by: datetime | None = None,
    status: str = "pending",
):
    return create_todo_item(
        db,
        user_id=user_id,
        title=title,
        description=description,
        complete_by=complete_by,
        status=status,
    )


def update_todo_item_service(db: Session, todo_id: int, payload: dict):
    return update_todo_item(db, todo_id, payload)


def delete_todo_item_service(db: Session, todo_id: int):
    return delete_todo_item(db, todo_id)
