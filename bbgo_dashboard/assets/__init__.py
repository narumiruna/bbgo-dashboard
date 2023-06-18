from dagster import Definitions
from dagster import FilesystemIOManager

from .assets import daily_num_trades
from .assets import nav_history_detail
from .assets import trades
from .resources import DatabaseResource

defs = Definitions(
    assets=[trades, daily_num_trades, nav_history_detail],
    resources={
        'db': DatabaseResource(),
        'io_manager': FilesystemIOManager(base_dir='data'),
    },
)
