import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from models.user import Base as UserBase
from models.good_night import Base as GoodNightBase
from models.good_morning import Base as GoodMorningBase

# Считываем URL базы данных из переменной окружения
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Собираем все метаданные
target_metadata = UserBase.metadata
target_metadata = GoodNightBase.metadata
target_metadata = GoodMorningBase.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()