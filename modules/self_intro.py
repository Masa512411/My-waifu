import random

def selfIntro(request_json):

    phrase = request_json["result"]["parameters"]["How_to_call"]

    with open("./date/profile.json","r") as f:
        ans = f.read()

    ans = json.loads(ans)
    try:
        speech = random.choice(ans[phrase])
    except KeyError:
        speech = "ちょっとわからないです"

    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-type'] = 'application/json'
    return(res)


