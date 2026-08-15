from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import CreateUserRequest, UpdateUserRequest, UserResponse
from app.services.user_service import (
    create_user_service,
    delete_user_service,
    get_user_service,
    list_users_service,
    update_user_service,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), skip: int = Query(0), limit: int = Query(100)):
    return list_users_service(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_service(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("", response_model=UserResponse)
def create_user_endpoint(user: CreateUserRequest, db: Session = Depends(get_db)):
    return create_user_service(db, user.gmail, user.username)


@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user: UpdateUserRequest, db: Session = Depends(get_db)):
    updated = update_user_service(db, user_id, user.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user_service(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
