import json
import os 
import datetime
import sys

import requests as req
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

from modules.intro_kosen import intro
from modules.weather_scraping import weather

app = Flask(__name__)

@app.route("/webhook",methods=["POST"])
def main():
    request_json = request.get_json()

    if request_json["result"]["metadata"]["intentName"] == "weather":
        res = weather(request_json)


    if request_json["result"]["metadata"]["intentName"] == "intro-kosen":
        res = intro(request_json)

    return(res)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    
    app.run(debug=False,port=port,host="0.0.0.0")

