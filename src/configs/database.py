from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.configs.settings import settings


engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False,)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
