from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateToDoItemRequest(BaseModel):
    title: str
    description: str | None = None
    complete_by: datetime | None = None
    status: str = "pending"
    user_id: int


class ToDoItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    complete_by: datetime | None = None
    created_on: datetime
    updated_on: datetime
    status: str
    user_id: int


class UpdateToDoItemRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    complete_by: datetime | None = None
    status: str | None = None


ToDoItemCreate = CreateToDoItemRequest
ToDoItemRead = ToDoItemResponse
ToDoItemUpdate = UpdateToDoItemRequest
