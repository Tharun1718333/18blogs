from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateEventRequest(BaseModel):
    user_id: int
    title: str
    description: str | None = None
    event_date: datetime


class EventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    title: str
    description: str | None = None
    event_date: datetime
    created_on: datetime
    updated_on: datetime


class UpdateEventRequest(BaseModel):
    user_id: int | None = None
    title: str | None = None
    description: str | None = None
    event_date: datetime | None = None


EventCreate = CreateEventRequest
EventRead = EventResponse
EventUpdate = UpdateEventRequest
