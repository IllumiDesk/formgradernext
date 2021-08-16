import os, jinja2
from traitlets import Unicode
from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin
from .handlers import ParameterHandler, TemplateHandler, IndexHandler, ErrorHandler

DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "static")
DEFAULT_TEMPLATE_FILES_PATH = os.path.join(os.path.dirname(__file__), "templates")

class LmsApp(ExtensionAppJinjaMixin, ExtensionApp):

    # The name of the extension.
    name = "IllumiDesk LMS application"

    # Te url that your extension will serve its homepage.
    extension_url = '/formgradernext'

    # Should your extension expose other server extensions when launched directly?
    load_other_extensions = True

    # Local path to static files directory.
    static_paths = [
        DEFAULT_STATIC_FILES_PATH
    ]

    # Local path to templates directory.
    template_paths = [
        DEFAULT_TEMPLATE_FILES_PATH
    ]

    def initialize_handlers(self):
        self.handlers.extend([
            (r'/formgradernext/params/(.+)$', ParameterHandler),
            (r'/formgradernext/template', TemplateHandler),
            (r'/formgradernext/?', IndexHandler),
            (r'/formgradernext/(.*)', ErrorHandler)
        ])

    def initialize_settings(self):
        self.log.info('Config {}'.format(self.config))

#-----------------------------------------------------------------------------
# Main entry point
#-----------------------------------------------------------------------------

main = launch_new_instance = LmsApp.launch_instance