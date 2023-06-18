from dagster import Definitions

from .resources import DatabaseResource
from .trades import daily_num_trades
from .trades import trades

defs = Definitions(
    assets=[trades, daily_num_trades],
    resources={'db': DatabaseResource()},
)
