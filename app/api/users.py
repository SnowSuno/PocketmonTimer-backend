from fastapi import APIRouter

from app.models import User
from app.queries import get_users_or_create

router = APIRouter()


@router.get("/{username}", response_model=User)
async def get_user_data(username: str) -> User:
    return get_users_or_create(username)


@router.post("/{username}/create", response_model=User)
async def create_pokemon(username: str):
    user = get_users_or_create(username)

    return user
