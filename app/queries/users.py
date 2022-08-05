from sqlmodel import Session, select

from app.core.database import engine
from app.models import User
from app.modules.github import get_github_commits


def get_users_or_create(username: str) -> User:
    commits = get_github_commits(username)

    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.username == username)
        ).one_or_none()

        if user is None:
            user = User(
                username=username,
                commits=commits,
                current_pokemon=None,
                current_commits=0,
                pokedex="",
            )

            session.add(user)
            session.commit()
            session.refresh(user)

    return user


def update_user_commits(user: User) -> User:
    commit_count = get_github_commits(user.username)

    with Session(engine) as session:
        user.current_commits = commit_count
        session.add(user)
        session.commit()
        session.refresh(user)

    return user
