import os
import requests
import sys

from jinja2 import Environment, BaseLoader
from tornado import web

from nbgrader.server_extensions.formgrader.base import (
    BaseHandler,
    check_xsrf,
    check_notebook_dir,
)

from notebook.notebookapp import NotebookApp
from notebook.utils import url_path_join as ujoin

DEFAULT_LMS_VERSION = os.environ.get("DEFAULT_LMS_VERSION") or "0.1.0"


def get_template(version):
    template_response = requests.get(
        f"https://content.illumidesk.com/lms/{version}/index.html"
    )
    return template_response.text.replace(
        "</head>", '<script>var base_url = "{{ base_url }}";</script></head>'
    )

class LMSHandler(BaseHandler):
    @web.authenticated
    @check_xsrf
    @check_notebook_dir
    def get(self):
        html = (
            Environment(loader=BaseLoader)
            .from_string(get_template(self.get_query_argument("lms_version", DEFAULT_LMS_VERSION)))
            .render(
                url_prefix=self.url_prefix,
                base_url=self.base_url,
                windows=(sys.prefix == "win32"),
                course_id=self.api.course_id,
                exchange=self.api.exchange,
                exchange_missing=self.api.exchange_missing,
            )
        )
        self.write(html)


handlers = [
    (r"/formgradernext.*", LMSHandler),
]


def rewrite(nbapp: NotebookApp, x):
    web_app = nbapp.web_app
    pat = ujoin(web_app.settings["base_url"], x[0].lstrip("/"))
    return (pat,) + x[1:]


def load_jupyter_server_extension(nbapp: NotebookApp):
    nbapp.web_app.add_handlers(".*$", [rewrite(nbapp, x) for x in handlers])
