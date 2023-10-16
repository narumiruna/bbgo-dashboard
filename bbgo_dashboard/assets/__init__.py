from dagster import Definitions
from dagster import FilesystemIOManager

from .assets import daily_num_trades
from .assets import nav_history_detail
from .assets import orders
from .assets import positions
from .assets import profits
from .assets import trades
from .resources import DatabaseResource

defs = Definitions(
    assets=[
        daily_num_trades,
        nav_history_detail,
        orders,
        positions,
        profits,
        trades,
    ],
    resources={
        "db": DatabaseResource(),
        "io_manager": FilesystemIOManager(base_dir="data"),
    },
)
