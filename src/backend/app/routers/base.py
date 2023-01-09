

from fastapi import APIRouter

from app.routers.api.base import api_router

base_router = APIRouter()
base_router.include_router(api_router, tags=["api"], prefix='/api')
