from app.routers.blogs import router as blogs_router
from app.routers.events import router as events_router
from app.routers.todos import router as todos_router
from app.routers.users import router as users_router

__all__ = ["users_router", "todos_router", "blogs_router", "events_router"]
