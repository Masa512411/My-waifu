import json
import os

import requests as req
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/webhook",methods=["POST"])
def intro():
    request_json = request.get_json()
    apart_data = request_json["result"]["parameters"]["kosen-department"]

    with open("sinario.json","r") as f:
        sinario = f.read()

    sinario = json.loads(sinario)
    
    try:
        speech = sinario[data]
    except KeyError:
        speech = "ちょっとわかりません"
    
    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return(res)


if __name__ == "__main__":
   # port = int(os.environ.get("PORT",5000))

    #app.run(debug=False,port=port,host="0.0.0.0")
    app.run()

