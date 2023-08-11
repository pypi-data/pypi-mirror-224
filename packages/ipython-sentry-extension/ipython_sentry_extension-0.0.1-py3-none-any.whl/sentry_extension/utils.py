from sentry_sdk.utils import BadDsn, Dsn


def is_valid_sentry_dsn(sentry_dsn: str) -> bool:
    try:
        Dsn(sentry_dsn)
    except BadDsn:
        return False
    else:
        return True
