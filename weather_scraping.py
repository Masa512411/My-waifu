import json
import os 
import datetime

import requests as req
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/webhook",methods=["POST"])
def main():
    req = request.get_json()
    date = req["queryResult"]["parameters"]["date"]
    weather = req["queryResult"]["parameters"]["weather"]
    url = "https://tenki.jp/forecast/7/37/6710/34100/"

    date = date.split("T")[0]
    
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)


    response = req.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text,"lxml")

    if date == datetime.strftime(today,"%Y-%m-%d"):
       today = soup.find(calss_="today-weather")
       forecast_weather = today.p.string
       speech = "今日の広島の天気は{}です".format(forecast_weather)
    elif data == datetime.strftime(tomorrow,"%Y-%m-%d"):
        tomorrow = soup.find(class_="tomorrow-weather")
        forcast_weather = tomorrow.p.string
        speech = "明日の広島の天気は{}です".format(forecast_weather)

    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return res


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    
    app.run(debug=False,port=port,host="0.0.0.0")



       

    
