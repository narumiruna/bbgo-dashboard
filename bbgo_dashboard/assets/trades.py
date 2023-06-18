import pandas as pd
from dagster import MetadataValue
from dagster import Output
from dagster import asset

from .resources import DatabaseResource


@asset
def trades(db: DatabaseResource) -> Output:
    df = db.read_sql('SELECT * FROM trades')
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })
