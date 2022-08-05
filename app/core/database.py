from sqlmodel import SQLModel, create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)


def init_db():
    """
    Create the database and tables.
    """
    SQLModel.metadata.create_all(engine)
