from typing import Optional

from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class UserBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    commits: int
    current_pokemon: str | None
    current_commits: int


class User(UserBase, table=True):
    pokedex: str


class ParsedUser(UserBase):
    pokedex: list[str]
