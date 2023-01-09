from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_cleanings():
    cleanings = [
        {
            "id": 1,
            "name": "My house",
            "clean_type": "full_clean",
            "price_per_hour": 29.99,
        },
    ]

    return cleanings
