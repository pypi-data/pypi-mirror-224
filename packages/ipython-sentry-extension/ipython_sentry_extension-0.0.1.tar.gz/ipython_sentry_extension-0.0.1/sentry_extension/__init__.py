# -----------------------------------------------------------
# Main IPython Sentry extension module
#
# (C) 2023 Pavel Komar / pvkomar@cloud.ru
# -----------------------------------------------------------
import os

import sentry_sdk
from IPython.core.interactiveshell import ExecutionResult, InteractiveShell

import sentry_extension.constants as const
from sentry_extension.utils import is_valid_sentry_dsn


def post_run_cell_cb(result: ExecutionResult) -> None:
    """
    Checks if any error occurred before or in cell's execution time.
    If so, sends event to Sentry
    """
    err = result.error_in_exec or result.error_before_exec

    if err:
        with sentry_sdk.push_scope() as scope:
            scope.set_extra(const.CELL_CONTEXT_EXTRA_KEY, result.info.raw_cell)
            sentry_sdk.capture_exception(err)


def load_ipython_extension(ip: InteractiveShell) -> None:
    """
    Initializes Sentry and registers callbacks in case if valid Sentry DSN
    was loaded from environment
    """
    _IPYTHON_SENTRY_DSN = os.getenv(const.IPYTHON_SENTRY_DSN_ENV_VAR)

    if is_valid_sentry_dsn(_IPYTHON_SENTRY_DSN):
        sentry_sdk.init(dsn=_IPYTHON_SENTRY_DSN, traces_sample_rate=1.0)

        # Callbacks registration
        ip.events.register(const.IPythonEvents.POST_RUN_CELL, post_run_cell_cb)
