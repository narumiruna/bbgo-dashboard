from dagster import Definitions
from dagster import asset

from .resources import DatabaseResource
from .trades import trades

defs = Definitions(
    assets=[trades],
    resources={'db': DatabaseResource()},
)
