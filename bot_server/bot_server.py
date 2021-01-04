# bot_server.py
# by Wesley Chui

from helpers import check_payload, parse_service_and_args_from, format_arguments
from services import services_dict, title, blurb, partype, attackrange, movespeed

import services
import traceback
from flask import Flask, request, render_template
from bot_harness import inspect_services


class ServiceArgumentError(Exception):
    pass

name, description, service_properties = inspect_services(services)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        try:
            service_name = request.form['service']
            service = getattr(services, service_name)
            service_args = get_service_args(service_name, request.form)
            print("Calling service {} with arguments: {}".format(service_name, service_args))
            service_response = service(**service_args)
            print("Result:".format(service_response))
            message = {
                "status": "success",
                "content": service_response
            }
        except IndexError:
            message = {"status": "error", "content": "There is no service called '{}'.".format(service_name)}
        except AttributeError:
            message = {"status": "error", "content": "The function '{}' is not defined in services.py".format(service_name)}
        except ServiceArgumentError as e:
            message = {"status": "error", "content": str(e)}
        except Exception as e:
            print(traceback.format_exc())
            message = {"status": "error", "content": "The function '{}' raised an error.".format(service_name)}
    else:
        message = None
        service_name = service_properties[0]['name']
        service_args = {}

    return render_template('index.html', name=name, description=description, services=service_properties, message=message, service_name=service_name, service_args=service_args)

def get_service_args(service_name, form):
    "Reads service arguments from the form and casts them to the appropriate type"
    props = [s for s in service_properties if s['name'] == service_name][0]
    args = {}
    for argname, argtype in props['arguments']:
        try:
            args[argname] = argtype(form[argname])
        except IndexError:
            raise ServiceArgumentError("Expected argument '{}'".format(argname))
        except ValueError:
            raise ServiceArgumentError("Could not parse '{}' value '{}' as type {}".format(argname, form[argname], argtype))
    return args


# parse message, format args, and check for errors in service and arguments
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
        return { "msg": title(arguments[0]) }
    elif service == "blurb":
        return { "msg": blurb(arguments[0]) }
    elif service == "partype":
        return { "msg": partype(arguments[0]) }
    elif service == "attackrange":
        return { "msg": attackrange(arguments[0]) }
    elif service == "movespeed":
        return { "msg": movespeed(arguments[0]) }
    else:
        return {"A service and champion is required to get results"}

@app.route('/help', methods=['GET'])
def help():
    message = "Hello! I'm the LoL bot. I can return the title, blurb,\n" \
            "partype, attackrange or movespeed of a certain champion that is in \n" \
            "League of Legends as of patch 10.24.\n" \
            "To use my services, send me a message containing a service and a \n" \
            "champion like \"title Zed\".\n" \
            "\n" \
            "Here are the commands you can use:\n" \
            "title [champion]\n" \
            "blurb [champion]\n" \
            "partype [champion]\n" \
            "attackrange [champion]\n" \
            "movespeed [champion]\n"
    return { "msg": message }

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
