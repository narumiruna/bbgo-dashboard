import os
from datetime import datetime
from datetime import timedelta

import pandas as pd
import plotly.express as px
import quantstats as qs
import streamlit as st
from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.engine import URL

from bbgo_dashboard.db import NavHistoryDetail
from bbgo_dashboard.db import Profit
from bbgo_dashboard.db import Trade


def create_url() -> URL:
    host = st.text_input('host', value=os.environ.get('MYSQL_HOST', 'localhost'))
    port = st.text_input('port', value=os.environ.get('MYSQL_PORT', 3306))
    username = st.text_input('username', value=os.environ.get('MYSQL_USERNAME', 'root'))
    password = st.text_input('password', value=os.environ.get('MYSQL_PASSWORD', ''), type='password')
    database = st.text_input('database', value=os.environ.get('MYSQL_DATABASE', 'bbgo'))

    if password == '':
        password = None

    return URL.create(
        'mysql+pymysql',
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )


def create_nav_chart(engine):
    st.header('Net Asset Value in USD')
    start = st.date_input('start', (datetime.now() - timedelta(days=365)).date())
    stmt = select(
        NavHistoryDetail.time,
        NavHistoryDetail.currency,
        NavHistoryDetail.net_asset_in_usd,
    ).where(NavHistoryDetail.session == 'ALL', NavHistoryDetail.time >= start)
    nav = pd.read_sql(stmt, engine)
    fig = px.area(nav, x='time', y='net_asset_in_usd', color='currency', line_group='currency')
    st.plotly_chart(fig)

    # plot nav pie chart
    last_nav = nav[nav['time'].iloc[-1] == nav['time']]
    fig = px.pie(last_nav, values='net_asset_in_usd', names='currency')
    st.plotly_chart(fig)

    # calculate sharpe ratio
    daily_nav = nav.groupby(['time']).sum().drop(columns=['currency']).resample('D').ffill()
    returns = daily_nav['net_asset_in_usd'].pct_change()
    sharpe = qs.stats.sharpe(returns, periods=365, annualize=True)
    st.text('Sharpe: {:.2f}'.format(sharpe))


def create_daily_profit_chart(engine):
    st.header('Daily Profit')
    profit_start = st.date_input('profit start', (datetime.now() - timedelta(days=365)).date())
    quote_currency = st.text_input('quote_currency', 'USDT')

    stmt = select(
        Profit.traded_at,
        Profit.profit,
        Profit.quote_quantity,
    ).where(Profit.traded_at >= profit_start, Profit.quote_currency == quote_currency)
    profit = pd.read_sql(stmt, engine)
    profit = profit.groupby(pd.Grouper(key='traded_at', freq='D')).sum()
    profit.reset_index(inplace=True)
    logger.debug('profit: {}', profit)

    fig = px.bar(profit, x='traded_at', y='profit')
    st.plotly_chart(fig)

    st.text('Total Profit: {:.2f}'.format(profit['profit'].sum()))


def create_daily_trade_chart(engine):
    st.header('Daily Trade')
    trade_start = st.date_input('trade start', (datetime.now() - timedelta(days=365)).date())

    stmt = select(
        Trade.traded_at,
        Trade.quote_quantity,
        Trade.side,
    ).where(Trade.traded_at >= trade_start)
    trade = pd.read_sql(stmt, engine)
    trade = trade.groupby([pd.Grouper(key='traded_at', freq='D'), 'side']).sum()
    trade.reset_index(inplace=True)
    logger.debug('trade: {}', trade)

    fig = px.bar(trade, x='traded_at', y='quote_quantity', color='side')
    st.plotly_chart(fig)

    st.text('Total Trade: {:.2f}'.format(trade['quote_quantity'].sum()))


def main():
    load_dotenv()

    st.title('BBGO Dashboard')

    st.header('MySQL Connection')
    url = create_url()

    try:
        engine = create_engine(url)
        engine.connect()
    except Exception as e:
        logger.error(e)
        return

    create_nav_chart(engine)
    create_daily_profit_chart(engine)
    create_daily_trade_chart(engine)


if __name__ == '__main__':
    main()
