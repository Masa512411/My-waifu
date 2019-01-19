import json
import os 
import datetime
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/modules')

import requests as req
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

from intro-kosen import intro
from weather_scraping import weather

app = Flask(__name__)

@app.route("/webhook",methods=["POST"])
def main():
    request_json = request.get_json()

    if request_json["result"]["metadata"]["intentName"] == "weather":
        res = weather()


    if request_json["result"]["metadata"]["intentName"] == "intro-kosen":
        res = intro()

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    
    app.run(debug=False,port=port,host="0.0.0.0")
