import os
import re
import sys

from tornado import web

from nbgrader.base import BaseHandler
from nbgrader.base import check_xsrf
from nbgrader.base import check_notebook_dir


class LmsTemplate(BaseHandler):
    """Render LMS app"""
    def get(self):
        raise web.HTTPError(404)


root_path = os.path.dirname(__file__)
template_path = os.path.join(root_path, 'templates')
static_path = os.path.join(root_path, 'static')

default_handlers = [
    (r"/formgradernext/?", web.StaticFileHandler, {'path': fonts_path}),
]



from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin, ExtensionHandlerJinjaMixin
from jupyter_server.utils import url_escape

class ParameterHandler(ExtensionHandlerMixin, JupyterHandler):
    def get(self, matched_part=None, *args, **kwargs):
        var1 = self.get_argument('var1', default=None)
        components = [x for x in self.request.path.split("/") if x]
        self.write('<h1>Hello LMS from handler.</h1>')
        self.write('<p>matched_part: {}</p>'.format(url_escape(matched_part)))
        self.write('<p>var1: {}</p>'.format(url_escape(var1)))
        self.write('<p>components: {}</p>'.format(components))

class BaseTemplateHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler): pass

class IndexHandler(BaseTemplateHandler):
    def get(self):
        self.log.debug(self.get_template('index.html'))
        self.write(self.render_template("index.html"))

class TemplateHandler(BaseTemplateHandler):
    def get(self, path):
        self.log.debug(self.get_template('lms.html'))
        self.write(self.render_template('lms.html', path=path))

class ErrorHandler(BaseTemplateHandler):
    def get(self, path):
        self.write(self.render_template('error.html'))