import importlib
import os
from logging.config import fileConfig

from {{data.app_name}}.db import Base
from sqlalchemy import engine_from_config, pool

from alembic import context


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
models_mod = config.get_main_option("models_module")
models = importlib.import_module(models_mod)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def include_name(name, type_, parent_names):
    if type_ == "table":
        return name in target_metadata.tables
    return True


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    url = url or os.getenv("SRV_SQL")
    version_table = config.get_main_option("version_table")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        include_name=include_name,
        dialect_opts={"paramstyle": "named"},
        version_table=version_table,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """

    cfg = config.get_section(config.config_ini_section)
    url = config.get_main_option("sqlalchemy.url")
    url = url or os.getenv("SRV_SQL")
    version_table = config.get_main_option("version_table")

    connectable = engine_from_config(
        cfg,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table=version_table,
            include_name=include_name,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
