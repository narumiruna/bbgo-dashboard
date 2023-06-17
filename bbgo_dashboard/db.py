# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, DECIMAL, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BinanceKline(Base):
    __tablename__ = 'binance_klines'
    __table_args__ = (
        Index('idx_kline_binance_unique', 'symbol', 'interval', 'start_time', unique=True),
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval')
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(12), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False)
    taker_buy_quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))


class Deposit(Base):
    __tablename__ = 'deposits'
    __table_args__ = (
        Index('txn_id', 'exchange', 'txn_id', unique=True),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False)
    asset = Column(String(10), nullable=False)
    address = Column(String(128), nullable=False, server_default=text("''"))
    amount = Column(DECIMAL(16, 8), nullable=False)
    txn_id = Column(String(256), nullable=False)
    time = Column(DATETIME(fsp=3), nullable=False)


class FtxKline(Base):
    __tablename__ = 'ftx_klines'
    __table_args__ = (
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval'),
        Index('idx_kline_ftx_unique', 'symbol', 'interval', 'start_time', unique=True)
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(20), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 4), nullable=False, server_default=text("'0.0000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False)
    taker_buy_quote_volume = Column(DECIMAL(32, 4), nullable=False, server_default=text("'0.0000'"))


class GooseDbVersion(Base):
    __tablename__ = 'goose_db_version'

    id = Column(BIGINT, primary_key=True, unique=True)
    version_id = Column(BigInteger, nullable=False)
    is_applied = Column(TINYINT(1), nullable=False)
    tstamp = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class Kline(Base):
    __tablename__ = 'klines'
    __table_args__ = (
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval'),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(12), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))


class KucoinKline(Base):
    __tablename__ = 'kucoin_klines'
    __table_args__ = (
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval'),
        Index('idx_kline_kucoin_unique', 'symbol', 'interval', 'start_time', unique=True)
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(12), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False)
    taker_buy_quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))


class MarginInterest(Base):
    __tablename__ = 'margin_interests'

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    asset = Column(String(24), nullable=False, server_default=text("''"))
    isolated_symbol = Column(String(24), nullable=False, server_default=text("''"))
    principle = Column(DECIMAL(16, 8), nullable=False)
    interest = Column(DECIMAL(20, 16), nullable=False)
    interest_rate = Column(DECIMAL(20, 16), nullable=False)
    time = Column(DATETIME(fsp=3), nullable=False)


class MarginLiquidation(Base):
    __tablename__ = 'margin_liquidations'
    __table_args__ = (
        Index('order_id', 'order_id', 'exchange', unique=True),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    symbol = Column(String(24), nullable=False, server_default=text("''"))
    order_id = Column(BIGINT, nullable=False)
    is_isolated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    average_price = Column(DECIMAL(16, 8), nullable=False)
    price = Column(DECIMAL(16, 8), nullable=False)
    quantity = Column(DECIMAL(16, 8), nullable=False)
    executed_quantity = Column(DECIMAL(16, 8), nullable=False)
    side = Column(String(5), nullable=False, server_default=text("''"))
    time_in_force = Column(String(5), nullable=False, server_default=text("''"))
    time = Column(DATETIME(fsp=3), nullable=False)


class MarginLoan(Base):
    __tablename__ = 'margin_loans'

    gid = Column(BIGINT, primary_key=True)
    transaction_id = Column(BIGINT, nullable=False, unique=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    asset = Column(String(24), nullable=False, server_default=text("''"))
    isolated_symbol = Column(String(24), nullable=False, server_default=text("''"))
    principle = Column(DECIMAL(16, 8), nullable=False)
    time = Column(DATETIME(fsp=3), nullable=False)


class MarginRepay(Base):
    __tablename__ = 'margin_repays'

    gid = Column(BIGINT, primary_key=True)
    transaction_id = Column(BIGINT, nullable=False, unique=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    asset = Column(String(24), nullable=False, server_default=text("''"))
    isolated_symbol = Column(String(24), nullable=False, server_default=text("''"))
    principle = Column(DECIMAL(16, 8), nullable=False)
    time = Column(DATETIME(fsp=3), nullable=False)


class MaxKline(Base):
    __tablename__ = 'max_klines'
    __table_args__ = (
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval'),
        Index('idx_kline_max_unique', 'symbol', 'interval', 'start_time', unique=True)
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(12), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False)
    taker_buy_quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))


class NavHistoryDetail(Base):
    __tablename__ = 'nav_history_details'
    __table_args__ = (
        Index('idx_nav_history_details', 'time', 'currency', 'exchange'),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(30), nullable=False)
    subaccount = Column(String(30), nullable=False)
    time = Column(DATETIME(fsp=3), nullable=False)
    currency = Column(String(12), nullable=False)
    net_asset_in_usd = Column(DECIMAL(32, 2), nullable=False, server_default=text("'0.00'"))
    net_asset_in_btc = Column(DECIMAL(32, 20), nullable=False, server_default=text("'0.00000000000000000000'"))
    balance = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    available = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    locked = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    session = Column(String(30), nullable=False)
    is_margin = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_isolated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    isolated_symbol = Column(String(30), nullable=False, server_default=text("''"))
    net_asset = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    borrowed = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    price_in_usd = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    interest = Column(DECIMAL(32, 20), nullable=False, server_default=text("'0.00000000000000000000'"))


class OkexKline(Base):
    __tablename__ = 'okex_klines'
    __table_args__ = (
        Index('idx_kline_okex_unique', 'symbol', 'interval', 'start_time', unique=True),
        Index('klines_end_time_symbol_interval', 'end_time', 'symbol', 'interval')
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(10), nullable=False)
    start_time = Column(DATETIME(fsp=3), nullable=False)
    end_time = Column(DATETIME(fsp=3), nullable=False)
    interval = Column(String(3), nullable=False)
    symbol = Column(String(12), nullable=False)
    open = Column(DECIMAL(20, 8), nullable=False)
    high = Column(DECIMAL(20, 8), nullable=False)
    low = Column(DECIMAL(20, 8), nullable=False)
    close = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    volume = Column(DECIMAL(20, 8), nullable=False, server_default=text("'0.00000000'"))
    closed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    last_trade_id = Column(INTEGER, nullable=False, server_default=text("'0'"))
    num_trades = Column(INTEGER, nullable=False, server_default=text("'0'"))
    quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))
    taker_buy_base_volume = Column(DECIMAL(32, 8), nullable=False)
    taker_buy_quote_volume = Column(DECIMAL(32, 8), nullable=False, server_default=text("'0.00000000'"))


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        Index('orders_symbol', 'exchange', 'symbol'),
        Index('orders_order_id', 'order_id', 'exchange', unique=True)
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    order_id = Column(BIGINT, nullable=False)
    client_order_id = Column(String(122), nullable=False, server_default=text("''"))
    order_type = Column(String(16), nullable=False)
    symbol = Column(String(20), nullable=False)
    status = Column(String(12), nullable=False)
    time_in_force = Column(String(4), nullable=False)
    price = Column(DECIMAL(16, 8), nullable=False)
    stop_price = Column(DECIMAL(16, 8), nullable=False)
    quantity = Column(DECIMAL(16, 8), nullable=False)
    executed_quantity = Column(DECIMAL(16, 8), nullable=False, server_default=text("'0.00000000'"))
    side = Column(String(4), nullable=False, server_default=text("''"))
    is_working = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    created_at = Column(DATETIME(fsp=3), nullable=False)
    updated_at = Column(DATETIME(fsp=3), nullable=False, server_default=text("CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3)"))
    is_margin = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_isolated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_futures = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class Position(Base):
    __tablename__ = 'positions'
    __table_args__ = (
        Index('trade_id', 'trade_id', 'side', 'exchange', unique=True),
    )

    gid = Column(BIGINT, primary_key=True)
    strategy = Column(String(32), nullable=False)
    strategy_instance_id = Column(String(64), nullable=False)
    symbol = Column(String(20), nullable=False)
    quote_currency = Column(String(10), nullable=False)
    base_currency = Column(String(10), nullable=False)
    average_cost = Column(DECIMAL(16, 8), nullable=False)
    base = Column(DECIMAL(16, 8), nullable=False)
    quote = Column(DECIMAL(16, 8), nullable=False)
    profit = Column(DECIMAL(16, 8))
    trade_id = Column(BIGINT, nullable=False)
    side = Column(String(4), nullable=False)
    exchange = Column(String(12), nullable=False)
    traded_at = Column(DATETIME(fsp=3), nullable=False)


class Profit(Base):
    __tablename__ = 'profits'

    gid = Column(BIGINT, primary_key=True)
    strategy = Column(String(32), nullable=False)
    strategy_instance_id = Column(String(64), nullable=False)
    symbol = Column(String(20), nullable=False)
    average_cost = Column(DECIMAL(16, 8), nullable=False)
    profit = Column(DECIMAL(16, 8), nullable=False)
    net_profit = Column(DECIMAL(16, 8), nullable=False)
    profit_margin = Column(DECIMAL(16, 8), nullable=False)
    net_profit_margin = Column(DECIMAL(16, 8), nullable=False)
    quote_currency = Column(String(10), nullable=False)
    base_currency = Column(String(10), nullable=False)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    is_futures = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_margin = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_isolated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    trade_id = Column(BIGINT, nullable=False, unique=True)
    side = Column(String(4), nullable=False, server_default=text("''"))
    is_buyer = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_maker = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    price = Column(DECIMAL(16, 8), nullable=False)
    quantity = Column(DECIMAL(16, 8), nullable=False)
    quote_quantity = Column(DECIMAL(16, 8), nullable=False)
    traded_at = Column(DATETIME(fsp=3), nullable=False)
    fee_in_usd = Column(DECIMAL(16, 8))
    fee = Column(DECIMAL(16, 8), nullable=False)
    fee_currency = Column(String(10), nullable=False)


class Reward(Base):
    __tablename__ = 'rewards'
    __table_args__ = (
        Index('uuid', 'exchange', 'uuid', unique=True),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    uuid = Column(String(32), nullable=False)
    reward_type = Column(String(24), nullable=False, server_default=text("''"))
    currency = Column(String(5), nullable=False)
    quantity = Column(DECIMAL(16, 8), nullable=False)
    state = Column(String(5), nullable=False)
    created_at = Column(DateTime, nullable=False)
    spent = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    note = Column(Text)


class Trade(Base):
    __tablename__ = 'trades'
    __table_args__ = (
        Index('trades_traded_at', 'traded_at', 'symbol', 'exchange', 'id', 'fee_currency', 'fee'),
        Index('trades_price_quantity', 'order_id', 'price', 'quantity'),
        Index('id', 'exchange', 'symbol', 'side', 'id', unique=True),
        Index('trades_id_traded_at', 'id', 'traded_at'),
        Index('trades_order_id_traded_at', 'order_id', 'traded_at')
    )

    gid = Column(BIGINT, primary_key=True)
    id = Column(BIGINT)
    order_id = Column(BIGINT, nullable=False)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    symbol = Column(String(20), nullable=False)
    price = Column(DECIMAL(16, 8), nullable=False)
    quantity = Column(DECIMAL(16, 8), nullable=False)
    quote_quantity = Column(DECIMAL(16, 8), nullable=False)
    fee = Column(DECIMAL(16, 8), nullable=False)
    fee_currency = Column(String(10), nullable=False)
    is_buyer = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_maker = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    side = Column(String(4), nullable=False, server_default=text("''"))
    traded_at = Column(DATETIME(fsp=3), nullable=False)
    is_margin = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_isolated = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    strategy = Column(String(32))
    pnl = Column(DECIMAL(10, 0))
    is_futures = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class Withdraw(Base):
    __tablename__ = 'withdraws'
    __table_args__ = (
        Index('txn_id', 'exchange', 'txn_id', unique=True),
    )

    gid = Column(BIGINT, primary_key=True)
    exchange = Column(String(24), nullable=False, server_default=text("''"))
    asset = Column(String(10), nullable=False)
    address = Column(String(128), nullable=False)
    network = Column(String(32), nullable=False, server_default=text("''"))
    amount = Column(DECIMAL(16, 8), nullable=False)
    txn_id = Column(String(256), nullable=False)
    txn_fee = Column(DECIMAL(16, 8), nullable=False, server_default=text("'0.00000000'"))
    txn_fee_currency = Column(String(32), nullable=False, server_default=text("''"))
    time = Column(DATETIME(fsp=3), nullable=False)
