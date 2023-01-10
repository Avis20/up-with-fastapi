import logging
from databases import Database

from app.settings import get_settings


logger = logging.getLogger(__name__)
settings = get_settings()


async def connect_to_db() -> None:
    print("\n\n")
    print(settings.DATABASE_URL)
    print("\n\n")
    database = Database(settings.DATABASE_URL, min_size=2, max_size=10)

    try:
        await database.connect()
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR")
