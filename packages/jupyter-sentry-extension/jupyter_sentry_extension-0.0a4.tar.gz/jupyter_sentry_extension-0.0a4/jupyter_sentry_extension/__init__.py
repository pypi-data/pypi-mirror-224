"""Sentry extension for Jupyter Server"""
__version__ = "0.0.a4"


def _jupyter_server_extension_points():
    return [
        {
            "module": "jupyter_sentry_extension.extension",
        }
    ]
