import typing as t
from enum import Enum


CELL_CONTEXT_EXTRA_KEY: t.Final[str] = "Cell content"
IPYTHON_SENTRY_DSN_ENV_VAR: t.Final[str] = "IPYTHON_SENTRY_DSN"


class IPythonEvents(str, Enum):
    POST_RUN_CELL = "post_run_cell"
