from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.event import CreateEventRequest, EventResponse, UpdateEventRequest
from app.services.event_service import (
    create_event_service,
    delete_event_service,
    get_event_service,
    list_events_service,
    update_event_service,
)

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[EventResponse])
def list_events(db: Session = Depends(get_db), skip: int = Query(0), limit: int = Query(100)):
    return list_events_service(db, skip=skip, limit=limit)


@router.get("/{event_id}", response_model=EventResponse)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = get_event_service(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("", response_model=EventResponse)
def create_event_endpoint(event: CreateEventRequest, db: Session = Depends(get_db)):
    return create_event_service(
        db,
        user_id=event.user_id,
        title=event.title,
        description=event.description,
        event_date=event.event_date,
    )


@router.put("/{event_id}", response_model=EventResponse)
def update_event_endpoint(event_id: int, event: UpdateEventRequest, db: Session = Depends(get_db)):
    updated = update_event_service(db, event_id, event.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated


@router.delete("/{event_id}")
def delete_event_endpoint(event_id: int, db: Session = Depends(get_db)):
    deleted = delete_event_service(db, event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}
