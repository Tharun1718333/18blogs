from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateUserRequest(BaseModel):
    gmail: str
    username: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    gmail: str
    username: str | None = None
    created_on: datetime
    updated_on: datetime


class UpdateUserRequest(BaseModel):
    gmail: str | None = None
    username: str | None = None


UserCreate = CreateUserRequest
UserRead = UserResponse
UserUpdate = UpdateUserRequest
