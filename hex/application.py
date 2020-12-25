from flask import Flask

from hex.configuration import configure_inject, configure_application
from hex.web.blueprints.post_blueprint import create_post_blueprint
from hex.web.error_handlers import handle_500


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(create_post_blueprint(), url_prefix='/api')
    application.register_error_handler(500, handle_500)

    return application
