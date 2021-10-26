import datetime
import logging

from flask import Flask
from flask import json

app = Flask(__name__)


@app.route('/status')
def status():
    app.logger.info(f"{datetime.datetime.utcnow()}, {metrics.__name__} endpoint was reached")

    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route('/metrics')
def metrics():
    app.logger.info(f"{datetime.datetime.utcnow()}, {metrics.__name__} endpoint was reached")

    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    return response


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')
