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
    request_json = request.get_json()

    if request_json["result"]["metadata"]["intentName"] == "weather":
        date = request_json["result"]["parameters"]["date"]
        weather = request_json["result"]["parameters"]["weather"]

        url = "https://tenki.jp/forecast/7/37/6710/34100/"


        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)

        response = req.get(url)
        soup = BeautifulSoup(response.text,"html.parser")

        if date == datetime.datetime.strftime(today,"%Y-%m-%d"):
            today_html = soup.find(class_="today-weather")
            forecast_weather = today_html.p.string
            if forecast_weather == "晴":
                forecast_weather = "晴れ"
                speech = "今日の広島の天気は{}です".format(forecast_weather)
        elif date == datetime.datetime.strftime(tomorrow,"%Y-%m-%d"):
            tomorrow_html = soup.find(class_="tomorrow-weather")
            forecast_weather = tomorrow_html.p.string
            if forecast_weather == "晴":
                forecast_weather = "晴れ"
                speech = "明日の広島の天気は{}です".format(forecast_weather)

    if request_json["result"]["metadata"]["intentName"] == "intro-kosen":
        depart_data = request_json["result"]["parameters"]["kosen-department"]
        building_data = request_json["result"]["parameters"]["kosen-building"]

        with open("sinario.json","r") as f:
            sinario = f.read()

        sinario = json.loads(sinario)

        try:
            if depart_data == "":
                speech = sinario[building_data]
            if building_data == "":
                speech = sinario[depart_data]
        except KeyError:
            speech = "ちょっとわかりません"

    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return(res)


if __name__ == "__main__":
    #port = int(os.environ.get("PORT",5000))
    
    #app.run(debug=False,port=port,host="0.0.0.0")
    app.run()
