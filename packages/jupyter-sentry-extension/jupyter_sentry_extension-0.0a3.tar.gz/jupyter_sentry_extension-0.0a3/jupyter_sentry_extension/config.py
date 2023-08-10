import os
import typing as t


JUPYTER_SERVER_SENTRY_DSN: t.Final[t.Optional[str]] = os.getenv("JUPYTER_SERVER_SENTRY_DSN")
