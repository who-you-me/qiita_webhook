# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, json

import requests

app = Flask(__name__)

@app.route("/item", methods=["POST"])
def item():
    data = json.loads(request.form)
    title = data["item"]["title"]

    url = "https://howtv.slack.com/services/hooks/incoming-webhook?token=a7niD6GIojyerGPS9BQDLcrA"
    payload = {"text": title}
    requests.post(url, data=json.dumps(payload))

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
