import sentry_sdk
from jupyter_server.serverapp import ServerApp
from sentry_sdk.integrations.tornado import TornadoIntegration

from .config import JUPYTER_SERVER_SENTRY_DSN
from .constants import SENTRY_IS_CONFIGURED_MSG, SENTRY_IS_NOT_CONFIGURED_MSG


def _load_jupyter_server_extension(serverapp: ServerApp) -> None:
    """
    This function is called when the extension is loaded.
    """
    if JUPYTER_SERVER_SENTRY_DSN:
        sentry_sdk.init(
            dsn=JUPYTER_SERVER_SENTRY_DSN,
            integrations=[TornadoIntegration()],
            traces_sample_rate=1.0,
        )
        serverapp.log.info(SENTRY_IS_CONFIGURED_MSG)
    else:
        serverapp.log.info(SENTRY_IS_NOT_CONFIGURED_MSG)
