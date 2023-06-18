from datetime import date
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st
from loguru import logger
from sqlalchemy import select

from bbgo_dashboard.db import NavHistoryDetail
from bbgo_dashboard.db import create_engine_from_env


def main():
    engine = create_engine_from_env()

    st.title('BBGO Dashboard')

    logger.info('plotting net asset value in USD')
    st.header('Net Asset Value in USD')
    start = st.date_input('start', date(2020, 1, 1))
    stmt = select(
        NavHistoryDetail.time,
        NavHistoryDetail.currency,
        NavHistoryDetail.net_asset_in_usd,
    ).where(NavHistoryDetail.session == 'ALL', NavHistoryDetail.time >= start)
    nav = pd.read_sql(stmt, engine)
    fig = px.area(nav, x="time", y="net_asset_in_usd", color="currency", line_group="currency")
    st.plotly_chart(fig)

    last_nav = nav[nav['time'].iloc[-1] == nav['time']]
    fig = px.pie(last_nav, values='net_asset_in_usd', names='currency')
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()
