from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_current_user')
def get_current_user():
    return jsonify(username="Bob",
                   email="bob@company.com",
                   id=12345)
