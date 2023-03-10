from uvicorn import run

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.base import base_router
from app.settings import get_settings
from app.handlers import create_start_app_handler


app = FastAPI()
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_event_handler("startup", create_start_app_handler())

app.include_router(base_router)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=settings.BACKEND_PORT, reload=True)
