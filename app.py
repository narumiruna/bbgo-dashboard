import streamlit as st

from bbgo_dashboard.utils import load_pickle


def main():
    st.title('BBGO Dashboard')
    df = load_pickle('data/daily_num_trades')
    st.bar_chart(df)


if __name__ == '__main__':
    main()
