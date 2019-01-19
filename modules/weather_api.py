import requests as req
import json

API_KEY = "71126af4a7ecbc5143f25d1432f68d42"
URL = "http://api.openweathermap.org/data/2.5/forecast"

response = req.get(URL + "?id=1862415&units=metric&cnt=3&APPID=%s" %API_KEY)

j = json.loads(response.text)

with open("weather-forecast.json","w") as f:
    f.write(response.text)

