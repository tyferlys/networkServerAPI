from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS
from src.database.database import Base
from src.database.models.Network import Network, User, NetworkReview
from src.database.models.Network import Tag
from src.database.models.NetworkLike import NetworkLike
from src.database.models.TagToNetwork import TagToNetwork


config = context.config
section = config.config_ini_section
config.set_section_option(section, "DB_HOST", DB_HOST)
config.set_section_option(section, "DB_POST", DB_PORT)
config.set_section_option(section, "DB_NAME", DB_NAME)
config.set_section_option(section, "DB_USER", DB_USER)
config.set_section_option(section, "DB_PASS", DB_PASS)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
