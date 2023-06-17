import pandas as pd
from dagster import asset

from ..db import create_engine_from_env


@asset
def trades():
    engine = create_engine_from_env()
    return pd.read_sql("SELECT * FROM trades", engine)
