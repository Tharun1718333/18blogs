from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.blog import CreateBlogRequest, BlogResponse, UpdateBlogRequest
from app.services.blog_service import (
    create_blog_service,
    delete_blog_service,
    get_blog_service,
    list_blogs_service,
    update_blog_service,
)

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("", response_model=list[BlogResponse])
def list_blogs(db: Session = Depends(get_db), skip: int = Query(0), limit: int = Query(100)):
    return list_blogs_service(db, skip=skip, limit=limit)


@router.get("/{blog_id}", response_model=BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog_service(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.post("", response_model=BlogResponse)
def create_blog_endpoint(blog: CreateBlogRequest, db: Session = Depends(get_db)):
    return create_blog_service(db, user_id=blog.user_id, blog_date=blog.blog_date, content=blog.content)


@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog_endpoint(blog_id: int, blog: UpdateBlogRequest, db: Session = Depends(get_db)):
    updated = update_blog_service(db, blog_id, blog.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated


@router.delete("/{blog_id}")
def delete_blog_endpoint(blog_id: int, db: Session = Depends(get_db)):
    deleted = delete_blog_service(db, blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}
