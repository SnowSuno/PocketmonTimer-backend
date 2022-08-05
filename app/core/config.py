from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Pokemon"
    BACKEND_CORS_ORIGINS: list = ["*"]
    DATABASE_URL: str = "sqlite:///data.db"


settings = Settings(_env_file=".env")
