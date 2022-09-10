from app.api.routes import (authentication, comments, ping, profiles, tags,
                            users)
from app.api.routes.items import api as items
from fastapi import APIRouter

router = APIRouter()
router.include_router(ping.router, prefix="/ping")
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
router.include_router(items.router, tags=["items"])
router.include_router(
    comments.router,
    tags=["comments"],
    prefix="/items/{slug}/comments",
)
router.include_router(tags.router, tags=["tags"], prefix="/tags")
