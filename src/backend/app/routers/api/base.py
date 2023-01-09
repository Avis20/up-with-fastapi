
from fastapi import APIRouter

from app.routers.api.v1 import cleanings

api_router = APIRouter()
api_router.include_router(cleanings.router, tags=["cleanings"], prefix='/cleanings')
