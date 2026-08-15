from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.event_repository import (
    create_event,
    delete_event,
    get_event,
    get_events,
    update_event,
)


def list_events_service(db: Session, skip: int = 0, limit: int = 100):
    return get_events(db, skip=skip, limit=limit)


def get_event_service(db: Session, event_id: int):
    return get_event(db, event_id)


def create_event_service(
    db: Session,
    user_id: int,
    title: str,
    event_date: datetime,
    description: str | None = None,
):
    return create_event(
        db,
        user_id=user_id,
        title=title,
        event_date=event_date,
        description=description,
    )


def update_event_service(db: Session, event_id: int, payload: dict):
    return update_event(db, event_id, payload)


def delete_event_service(db: Session, event_id: int):
    return delete_event(db, event_id)
