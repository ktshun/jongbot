from flask import Flask
import app

##app = Flask(__name__)

if __name__ == "__main__":
    ##app.register_blueprint(SlackController.app, url_prefix = '/slack')
    app = app.create_app()
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
