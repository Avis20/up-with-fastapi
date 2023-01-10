from typing import Callable

from app.connectors.database import connect_to_db


def create_start_app_handler() -> Callable:
    async def start_app() -> None:
        await connect_to_db()

    return start_app
