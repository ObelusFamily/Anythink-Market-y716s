from app.api.routes.items import items_common
from app.api.routes.items import items_resource
from fastapi import APIRouter

router = APIRouter()

router.include_router(items_common.router, prefix="/items")
router.include_router(items_resource.router, prefix="/items")
