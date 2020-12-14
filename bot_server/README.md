# Bot Server

## Accessing the bot
To access the bot, you should follow the instructions below to run the bot server and access
it either locally or remotely.

### Running the Bot server
```
$ bash run.sh
```

### Accessing the server from your local computer
After running the server, you will be able to send HTTP requests to `http://localhost:5000`

Your can test the server locally by running the following command in your terminal:
```
$ http get http://localhost:5000/
HTTP/1.0 200 OK
Content-Length: 32
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Nov 2020 08:26:43 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

Hello from the LoL bot!
```

### Accessing the server from another computer
Another computer on the same wifi network can access your bot server by using your IP address.

On a Mac, find your IP address by running the following command in your terminal:
```
$ ipconfig getifaddr en0
192.168.XX.XX
```

Give your IP address to your friend, and on their computer they can run the following command in their terminal:
(Be sure to replace the XXX with the numbers you found for your IP address!)
```
$ http get http://192.168.XXX.XX:5000/
HTTP/1.0 200 OK
Content-Length: 32
Content-Type: text/html; charset=utf-8
Date: Wed, 18 Nov 2020 08:26:43 GMT
Server: Werkzeug/1.0.1 Python/3.8.5

Hello, this is the LoL bot!
```

## Services

| Service  | Description                                                                                   | API Route   | Message Platform Command | Parameters (with  types)                                                                                                                                        | Example Usage       | Returns                                |
|----------|-----------------------------------------------------------------------------------------------|-------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------|
| title      | gives the title of the champion given | `/title`      | `title champion`            | `champion` (`string`):  a champion from patch 10.24 or before    | title Zed             | `{ "champion": title of champion }`             |
| blurb      | gives the blurb of the champion given | `/blurb`      | `blurb champion`            | `champion` (`string`):  a champion from patch 10.24 or before    | blurb Zed             | `{ "champion": blurb of champion }`             |
| partype      | gives the partype of the champion given | `/partype`      | `partype champion`            | `champion` (`string`):  a champion from patch 10.24 or before    | partype Zed             | `{ "champion": partype of champion }`
| attackrange      | gives the attackrange of the champion given | `/attackrange`      | `attackrange champion`            | `champion` (`string`):  a champion from patch 10.24 or before    | attackrange Zed             | `{ "champion": blurb of champion }`
| movespeed      | gives the movespeed of the champion given | `/movespeed`      | `movespeed champion`            | `champion` (`string`):  a champion from patch 10.24 or before    | movespeed Zed             | `{ "champion": movespeed of champion }`  


## Files
Here's an overview of the files in the directory and what you should do with them.

### `bot_server.py`
This file will define the routes for your message bot. The bot should be able
to serve routes for the following endpoints:

* `/` (`GET`) - This route just helps us know if the server is running. Nothing to
change here.
* `/message` (`POST`) - This route recieves a message from the message server, triggers
the bot's service, and responds appropriately based on the service requested. Currently,
the route parses the message sent to the bot into the `service` requested and a list
of `arguments` passed with the message. Additionally, the route checks the formatting of
the service request and generates an error if anything is wrong. However, currently the
route can only respond to a request for help.
* `/help` (`GET`) - This route should return a message describing to a user what your bot
does and how to use it.
* `/<title>` (`GET`) - ** The title function returns the title when given the argument of a champion.
  Firstly it deletes any spaces or apostrophes if any are found in the argument,
  then it makes the string lower case and converts the 1st letter into upper case
  then processes the argument and returns the title of a champion.
* `/<blurb>` (`GET`) - ** The blurb function returns the blurb when given the argument of a champion.
  Firstly it deletes any spaces or apostrophes if any are found in the argument,
  then it makes the string lower case and converts the 1st letter into upper case
  then processes the argument and returns the blurb of a champion.
* `/<partype>` (`GET`) - ** The partype function returns the partype when given the argument of a champion.
  Firstly it deletes any spaces or apostrophes if any are found in the argument,
  then it makes the string lower case and converts the 1st letter into upper case
  then processes the argument and returns the partype of a champion.
* `/<attackrange>` (`GET`) - ** The attackrange function returns the attackrange when given the argument of a champion.
  Firstly it deletes any spaces or apostrophes if any are found in the argument,
  then it makes the string lower case and converts the 1st letter into upper case
  then processes the argument and returns the attackrange of a champion.
* `/<movespeed>` (`GET`) - ** The movespeed function returns the movespeed when given the argument of a champion.
  Firstly it deletes any spaces or apostrophes if any are found in the argument,
  then it makes the string lower case and converts the 1st letter into upper case
  then processes the argument and returns the movespeed of a champion.

### `services.py`
This module defines functions for each of the services your bot provides.

```
services_dict = {
        "help":[],
        "partype": [str],
        "blurb": [str],
        "title": [str],
        "attackrange": [str],
        "movespeed": [str],
}

```

### `helpers.py`
This module contains helper functions used by the bot server.

#### `check_payload(values_dict, expected)`
Ensures that the data sent with an HTTP request
contains all expected params and no unexpected params.

<ins>Parameters:</ins>
* `values_dict` - a dictionary of values sent with the HTTP request
* `expected` - a list of the values expected in the `values_dict`

<ins>Returns:</ins>
* a list of errors found while checking payload (empty list implies no errors in payload)

#### `parse_service_and_args_from(msg, services_dict)`
Parses the message, `msg`, sent to the bot into the service and the arguments for the service,
formats the arguments and checks for errors, and returns serivce, arguments, and errors as a tuple.
Arguments in the `msg` should be single words, separated by spaces (execpt for the last argument).
Arguments will be returned as a list of values based on the expected values defined in the `services_dict`.

<ins>Parameters:</ins>
* `msg` - string contain service and arguments separated by single spaces
* `services_dict` - dictionary with each service provided by the bot as a string paired with a list of the types
that service requires

<ins>Returns:</ins>
* a tuple containing:
  * the single word service string
  * a list of single word argument strings
  * a list of error strings

#### `format_arguments(service, args, services_dict)`
Checks to make sure the arguements, `args`, are valid given the defintions in the `services_dict` and
formats the arguments into the types defined in the `services_dict`. A description of errors found is placed into the
errors list and returned

<ins>Parameters:</ins>
* `service` - single word string containing the service
* `args` - list of single word strings containing the arguments for the service
* `services_dict` - dictionary with each service provided by the bot as a string paired with a list of the types
that service requires

<ins>Returns:</ins>
* a tuple containing:
  * the list of formatted arguments
  * a list of error strings
