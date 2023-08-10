import os

import sentry_sdk
from jupyter_server.serverapp import ServerApp
from sentry_sdk.integrations.tornado import TornadoIntegration


def _load_jupyter_server_extension(serverapp: ServerApp) -> None:
    """
    This function is called when the extension is loaded.
    """
    _JUPYTER_SERVER_SENTRY_DSN = os.getenv("JUPYTER_SERVER_SENTRY_DSN")

    if _JUPYTER_SERVER_SENTRY_DSN:
        sentry_sdk.init(
            dsn=_JUPYTER_SERVER_SENTRY_DSN,
            integrations=[TornadoIntegration()],
            traces_sample_rate=1.0,
        )
        serverapp.log.info("Sentry is configured!")
    else:
        serverapp.log.info("Sentry is not configured:(")
