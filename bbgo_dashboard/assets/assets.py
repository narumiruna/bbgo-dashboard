import pandas as pd
from dagster import MetadataValue
from dagster import Output
from dagster import asset
from sqlalchemy import select

from ..db import NavHistoryDetail
from ..db import Order
from ..db import Position
from ..db import Profit
from ..db import Trade
from .resources import DatabaseResource


@asset
def trades(db: DatabaseResource) -> Output[pd.DataFrame]:
    df = db.read_sql(select(Trade), parse_dates=['traded_at'])
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def daily_num_trades(trades: pd.DataFrame) -> Output[pd.DataFrame]:
    df = trades.groupby([pd.Grouper(freq='D'), 'side']).count()
    df = df[['gid']]
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def nav_history_detail(db: DatabaseResource) -> Output[pd.DataFrame]:
    df = db.read_sql(select(NavHistoryDetail), parse_dates=['time'])
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def profits(db: DatabaseResource) -> Output[pd.DataFrame]:
    df = db.read_sql(select(Profit), parse_dates=['traded_at'])
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def positions(db: DatabaseResource) -> Output[pd.DataFrame]:
    df = db.read_sql(select(Position), parse_dates=['traded_at'])
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })


@asset
def orders(db: DatabaseResource) -> Output[pd.DataFrame]:
    df = db.read_sql(select(Order), parse_dates=['created_at', 'updated_at'])
    return Output(value=df,
                  metadata={
                      "len_df": MetadataValue.int(len(df)),
                      "preview": MetadataValue.md(df.head().to_markdown()),
                  })
