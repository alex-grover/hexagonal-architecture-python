from flask import Flask

from hex.configuration import configure_inject, configure_application
from hex.web.post_blueprint import create_post_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)

    application.register_blueprint(create_post_blueprint(), url_prefix='/api')

    return application
