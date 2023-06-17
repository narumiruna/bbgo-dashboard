import os

import pandas as pd
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def create_url_from_env(drivername: str = 'mysql+pymysql'):
    return URL.create(
        drivername,
        username=os.environ.get('MYSQL_USERNAME', 'root'),
        password=os.environ.get('MYSQL_PASSWORD'),
        host=os.environ.get('MYSQL_HOST', 'localhost'),
        port=os.environ.get('MYSQL_PORT', 3306),
        database=os.environ.get('MYSQL_DATABASE', 'bbgo'),
    )


def create_engine_from_env(**kwargs):
    return create_engine(create_url_from_env(), **kwargs)
