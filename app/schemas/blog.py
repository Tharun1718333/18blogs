from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateBlogRequest(BaseModel):
    user_id: int
    blog_date: datetime
    content: str


class BlogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    blog_date: datetime
    content: str
    created_on: datetime
    updated_on: datetime


class UpdateBlogRequest(BaseModel):
    user_id: int | None = None
    blog_date: datetime | None = None
    content: str | None = None


BlogCreate = CreateBlogRequest
BlogRead = BlogResponse
BlogUpdate = UpdateBlogRequest
