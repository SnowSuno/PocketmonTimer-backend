import json

from fastapi import APIRouter

from app.models import User, ParsedUser
from app.queries import get_users_or_create, update_user_commits

router = APIRouter()


@router.get("/{username}", response_model=ParsedUser)
async def get_user_data(username: str) -> ParsedUser:
    user = get_users_or_create(username)
    user = update_user_commits(user)

    user_dict = user.dict()
    user_dict.pop("pokedex")

    return ParsedUser(
        **user_dict,
        pokedex=json.loads(user.pokedex)
    )


@router.post("/{username}/create", response_model=User)
async def create_pokemon(username: str):
    user = get_users_or_create(username)

    return user
