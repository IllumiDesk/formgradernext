"""Tornado handlers for nbgrader background service."""
import os

from .server_extensions.formgrader.handlers import load_jupyter_server_extension


def _jupyter_nbextension_paths():
    return [
        dict(
            section="tree",
            src=os.path.join('nbextensions', 'formgrader'),
            dest="formgrader",
            require="formgrader/main"
        ),
    ]

def _jupyter_server_extension_paths():
    return [
        dict(module="async_nbgrader"),
        dict(module="async_nbgrader.server_extensions.formgrader"),
    ]
