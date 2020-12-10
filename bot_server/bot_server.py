# bot_server.py
# by

from flask import Flask, request
from helpers import check_payload, parse_service_and_args_from, format_arguments
from services import services_dict, title, blurb, partype, attackrange, movespeed

app = Flask(__name__)


# parse message, format args, and check for errors in service and arguments
@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is the LoL_bot!"


@app.route('/message', methods=['POST'])
def new_message():
    data = request.get_json()

    # check for errors in payload
    errors = check_payload(data, ["sender", "msg", "timestamp"])
    if len(errors) > 0:
        return {"errors": errors}, 400

    # parse message, format args, and check for errors in service and arguments
    msg = data["msg"]
    service, arguments, errors = parse_service_and_args_from(msg, services_dict)
    if len(errors) > 0:
        return {"A service and champion is required to get results": errors}, 400

    if service == "help":
        return { "msg": help() }
    elif service == "title":
        return { "msg": title(arguments[0], arguments[1]) }
    elif service == "blurb":
        return { "msg": blurb(arguments[0], arguments[1]) }
    elif service == "partype":
        return { "msg": partype(arguments[0], arguments[1]) }
    elif service == "attackrange":
        return { "msg": attackrange(arguments[0], arguments[1]) }
    elif service == "movespeed":
        return { "msg": movespeed(arguments[0], arguments[1]) }
    else:
        return {"A service and champion is required to get results"}

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
    champion = str(data['champion'])
    atkrange = attackrange(champion)
    return { "champion": atkrange }

@app.route('/movespeed', methods=['GET'])
def movespeed_wrapper():
    data = request.get_json()
    errors = check_payload(data, ["champion"])
    if len(errors) > 0:
        return {"errors": errors}, 400
    champion = str(data['champion'])
    ms = movespeed(champion)
    return { "champion": ms }
