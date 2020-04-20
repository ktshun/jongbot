from flask import Blueprint

app = Blueprint('app', __name__)

@app.route('/deal')
def deal():
    return '配牌'
