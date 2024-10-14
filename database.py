import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL') or os.getenv('DATABASE_PUBLIC_URL')
print(DATABASE_URL)
if not DATABASE_URL:
    raise ValueError("Not database")
#БАзовый класс для моделей
Base = declarative_base()

#асинхронный движок для подключения к бд
engine = create_async_engine(DATABASE_URL, echo=True)

#Асинхронная сессия для работы с бд
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    """
    Функция для инициализации бд и созадния таблиц

    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session