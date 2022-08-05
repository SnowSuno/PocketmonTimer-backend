from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    commits: int
    current_pokemon: str | None
    current_commits: int
    pokedex: list[str]
