# bot_server.py
# by

from flask import Flask, request
from helpers import check_payload, parse_service_and_args_from, format_arguments
from services import services_dict, title, blurb, partype

app = Flask(__name__)

@app.route('/title', methods=['GET'])
def title_wrapper():
    data = request.get_json()
    errors = check_payload(data, ["champion"])
    if len(errors) > 0:
        return {"errors": errors}, 400
    champion = str(data['champion'])
    ttl = title(champion)
    return { "champion": ttl }


@app.route('/blurb', methods=['GET'])
def blurb_wrapper():
    data = request.get_json()
    errors = check_payload(data, ["champion"])
    if len(errors) > 0:
        return {"errors": errors}, 400
    champion = str(data['champion'])
    blb = blurb(champion)
    return { "champion": blb }


@app.route('/partype', methods=['GET'])
def partype_wrapper():
    data = request.get_json()
    errors = check_payload(data, ["champion"])
    if len(errors) > 0:
        return {"errors": errors}, 400
    champion = str(data['champion'])
    pt = partype(champion)
    return { "champion": pt }

@app.route('/attackrange', methods=['GET'])
def attackrange_wrapper():
    data = request.get_json()
    errors = check_payload(data, ["champion"])
    if len(errors) > 0:
        return {"errors": errors}, 400
    #champion = int(data[champion[stats["attackrange"]]])
    champion = str(data['champion'])
    atkrange = attackrange(champion)
    return { "champion": atkrange }
