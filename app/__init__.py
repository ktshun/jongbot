import os

from flask import Flask
from app.controller import slack


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # Load config files
    #app.config.from_pyfile("config/base_config.py")
    #if "ops_config" in os.environ:
    #    app.config.from_pyfile("config/%s_config.py" % (os.environ['ops_config']))

    app.register_blueprint(slack.app, url_prefix = '/slack')

    return app
