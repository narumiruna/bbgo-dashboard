from dagster import Definitions
from dagster import asset

from .trades import trades

defs = Definitions(assets=[trades])
