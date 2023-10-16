import os

from sqlalchemy import create_engine


def create_engine_from_env(**kwargs):
    db_url = os.environ.get("DB_URL", "mysql+pymysql://root@localhost/bbgo")
    return create_engine(db_url, **kwargs)
