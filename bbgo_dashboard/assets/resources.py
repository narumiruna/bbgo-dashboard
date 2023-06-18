import pandas as pd
from dagster import ConfigurableResource

from ..db import create_engine_from_env


class DatabaseResource(ConfigurableResource):

    def read_sql(self, sql, **kwargs) -> pd.DataFrame:
        engine = create_engine_from_env()
        df = pd.read_sql(sql, engine, **kwargs)
        return df
