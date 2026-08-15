from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.todo_item import (
    CreateToDoItemRequest,
    ToDoItemResponse,
    UpdateToDoItemRequest,
)
from app.services.todo_item_service import (
    create_todo_item_service,
    delete_todo_item_service,
    get_todo_item_service,
    list_todo_items_service,
    update_todo_item_service,
)

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("", response_model=list[ToDoItemResponse])
def list_todo_items(db: Session = Depends(get_db), skip: int = Query(0), limit: int = Query(100)):
    return list_todo_items_service(db, skip=skip, limit=limit)


@router.get("/{todo_id}", response_model=ToDoItemResponse)
def read_todo_item(todo_id: int, db: Session = Depends(get_db)):
    todo_item = get_todo_item_service(db, todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo_item


@router.post("", response_model=ToDoItemResponse)
def create_todo_item_endpoint(todo_item: CreateToDoItemRequest, db: Session = Depends(get_db)):
    return create_todo_item_service(
        db,
        user_id=todo_item.user_id,
        title=todo_item.title,
        description=todo_item.description,
        complete_by=todo_item.complete_by,
        status=todo_item.status,
    )


@router.put("/{todo_id}", response_model=ToDoItemResponse)
def update_todo_item_endpoint(todo_id: int, todo_item: UpdateToDoItemRequest, db: Session = Depends(get_db)):
    updated = update_todo_item_service(db, todo_id, todo_item.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return updated


@router.delete("/{todo_id}")
def delete_todo_item_endpoint(todo_id: int, db: Session = Depends(get_db)):
    deleted = delete_todo_item_service(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"message": "Todo item deleted successfully"}
