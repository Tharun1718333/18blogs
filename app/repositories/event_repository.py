from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Event


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


def create_event(
    db: Session,
    user_id: int,
    title: str,
    event_date: datetime,
    description: str | None = None,
):
    event = Event(user_id=user_id, title=title, event_date=event_date, description=description)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def update_event(db: Session, event_id: int, payload: dict):
    event = get_event(db, event_id)
    if not event:
        return None

    for key, value in payload.items():
        if value is not None:
            setattr(event, key, value)

    db.commit()
    db.refresh(event)
    return event


def delete_event(db: Session, event_id: int):
    event = get_event(db, event_id)
    if not event:
        return False

    db.delete(event)
    db.commit()
    return True
