from datetime import date

import pandas as pd
import plotly.express as px
import quantstats as qs
import streamlit as st
from sqlalchemy import select

from bbgo_dashboard.db import NavHistoryDetail
from bbgo_dashboard.db import create_engine_from_env


def main():
    engine = create_engine_from_env()

    st.title('BBGO Dashboard')

    # plot net asset value
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

    # plot nav pie chart
    last_nav = nav[nav['time'].iloc[-1] == nav['time']]
    fig = px.pie(last_nav, values='net_asset_in_usd', names='currency')
    st.plotly_chart(fig)

    # calculate sharpe ratio
    daily_nav = nav.groupby(['time']).sum().drop(columns=['currency']).resample('D').ffill()
    returns = daily_nav['net_asset_in_usd'].pct_change()
    sharpe = qs.stats.sharpe(returns, periods=365, annualize=True)
    st.text('Sharpe: {:.2f}'.format(sharpe))


if __name__ == '__main__':
    main()
