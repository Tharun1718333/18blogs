from datetime import datetime

from sqlalchemy.orm import Session

from app.models import ToDoItem


def get_todo_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ToDoItem).offset(skip).limit(limit).all()


def get_todo_item(db: Session, todo_id: int):
    return db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()


def create_todo_item(
    db: Session, user_id: int, title: str, description: str | None = None,
    complete_by: datetime | None = None, status: str = "pending"
):
    todo_item = ToDoItem(
        user_id=user_id,
        title=title,
        description=description,
        complete_by=complete_by,
        status=status,
    )
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item


def update_todo_item(db: Session, todo_id: int, payload: dict):
    todo_item = get_todo_item(db, todo_id)
    if not todo_item:
        return None

    for key, value in payload.items():
        if value is not None:
            setattr(todo_item, key, value)

    db.commit()
    db.refresh(todo_item)
    return todo_item


def delete_todo_item(db: Session, todo_id: int):
    todo_item = get_todo_item(db, todo_id)
    if not todo_item:
        return False

    db.delete(todo_item)
    db.commit()
    return True
