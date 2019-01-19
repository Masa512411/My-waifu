import random
import json

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response


def selfIntro(request_json):

    phrase = request_json["result"]["parameters"]["How_to_call"]

    with open("./data/profile.json","r") as f:
        ans = f.read()

    ans = json.loads(ans)
    try:
        speech = random.choice(ans[phrase])
    except KeyError:
        speech = "ちょっとわからないです"

    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return(res)


