from sqlmodel import Session, select

from app.core.database import engine
from app.models import User


def get_users_or_create(username: str) -> User:
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.username == username)
        ).one_or_none()

        if user is None:
            user = User(
                username=username,
                commits=0,
                current_pokemon_id=None,
                current_commits=0,
                pokedex="[]",
            )

            session.add(user)
            session.commit()
            session.refresh(user)
    return user
