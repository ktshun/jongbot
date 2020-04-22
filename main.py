from flask import Flask
import app

if __name__ == "__main__":
    app = app.create_app()
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
