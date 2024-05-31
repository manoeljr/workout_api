from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL = Field(default="postgresql+asyncpg://workout:workout@localhost/workout")


settings = Settings()
