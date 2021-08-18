"""Tornado handlers for formgrader custom UI."""
import os

from .handlers import load_jupyter_server_extension


def _jupyter_nbextension_paths():
    return [
        dict(
            section="common",
            src="static",
            dest="formgradernext",
            require="formgradernext/common"
        ),
    ]

def _jupyter_server_extension_paths():
    return [
        dict(module="formgradernext"),
    ]
