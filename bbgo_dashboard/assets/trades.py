import pandas as pd
from dagster import MetadataValue
from dagster import Output
from dagster import asset

from .resources import DatabaseResource


@asset
def trades(db: DatabaseResource) -> Output:
    df = db.read_sql('SELECT * FROM trades', parse_dates=['traded_at'])
    df.set_index('traded_at', inplace=True)
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def daily_num_trades(trades: pd.DataFrame):
    df = trades.groupby(pd.Grouper(freq='D')).count()
    df = df[['id']]
    df.columns = ['num_trades']
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })
