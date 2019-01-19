import json
import os

import requests as req
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response


def intro(request_json):
    apart_data = request_json["result"]["parameters"]["kosen-department"]

    with open("./modules/sinario.json","r") as f:
        sinario = f.read()

    sinario = json.loads(sinario)
    
    try:
        speech = sinario[data]
    except KeyError:
        speech = "ちょっとわかりません"
    
    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return(res)

