# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import request, json

import requests

app = Flask(__name__)

@app.route("/item", methods=["POST"])
def item():
    data = request.json
    title = data["item"]["title"]

    url = os.environ["SLACK_URL"]
    payload = {"text": title}
    requests.post(url, data=json.dumps(payload))

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
