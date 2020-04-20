import os

from flask import Flask
from app.controller import SlackController


def create_app():
    # create and configure the app
    app = Flask(__name__)

    # Load config files
    app.config.from_pyfile("config/baseConfig.py")
    env = os.getenv('FLASK_ENV', None)
    if env != None:
        app.config.from_pyfile("config/%sConfig.py" % env)

    app.register_blueprint(SlackController.app, url_prefix = '/slack')

    return app
