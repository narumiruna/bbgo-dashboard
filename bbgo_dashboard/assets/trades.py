import pandas as pd
from dagster import MetadataValue
from dagster import Output
from dagster import asset
from sqlalchemy import select

from ..db import Trade
from .resources import DatabaseResource


@asset
def trades(db: DatabaseResource) -> Output:
    df = db.read_sql(select(Trade), parse_dates=['traded_at'])
    df.set_index('traded_at', inplace=True)
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def daily_num_trades(trades: pd.DataFrame):
    df = trades.groupby([pd.Grouper(freq='D'), 'side']).count()
    df = df[['gid']]
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })
