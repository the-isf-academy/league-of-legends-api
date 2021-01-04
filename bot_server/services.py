# service.py
# This file should contain the functions used to run your service.
#
# Author: Wesley Chui
import requests
# service provided and expected arguments
services_dict = {
        "help":[],
        "partype": [str],
        "blurb": [str],
        "title": [str],
        "attackrange": [str],
        "movespeed": [str],
}

def title(champion):
    """
    The title function returns the title when given the argument of a champion.
    Firstly it deletes any spaces or apostrophes if any are found in the argument,
    then it makes the string lower case and converts the 1st letter into upper case
    then processes the argument and returns the title of a champion
    """
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe

    champion = champion.casefold() #converts string into lower case
    champion = champion.capitalize() #converts 1st letter into upper case

    if champion == 'Reksai' or champion == 'Kogmaw':
        champion = champion.replace("s","S") #if there is an s in the champion it replaces it with a capital S
        champion = champion.replace("m","M") #if there is an m in the champion it replaces it with a capital M
    else:
        pass

    champion = data[champion] #finds dictionary of champion inside data
    title = champion["title"] #finds dictionary of title inside champion
    return title

def blurb(champion):
    """
    The blurb function returns the blurb when given the argument of a champion.
    Firstly it deletes any spaces or apostrophes if any are found in the argument,
    then it makes the string lower case and converts the 1st letter into upper case
    then processes the argument and returns the blurb of a champion
    """
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe

    champion = champion.casefold() #converts string into lower case
    champion = champion.capitalize() #converts 1st letter into upper case

    if champion == 'Reksai' or champion == 'Kogmaw':
        champion = champion.replace("s","S") #if there is an s in the champion it replaces it with a capital S
        champion = champion.replace("m","M") #if there is an m in the champion it replaces it with a capital M
    else:
        pass

    champion = data[champion] #finds dictionary of champion inside data
    blurb = champion["blurb"] #finds dictionary of blurb inside champion
    return blurb

def partype(champion):
    """
    The partype function returns the partype when given the argument of a champion.
    Firstly it deletes any spaces or apostrophes if any are found in the argument,
    then it makes the string lower case and converts the 1st letter into upper case
    then processes the argument and returns the partype of a champion
    """
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe

    champion = champion.casefold() #converts string into lower case
    champion = champion.capitalize() #converts 1st letter into upper case

    if champion == 'Reksai' or champion == 'Kogmaw':
        champion = champion.replace("s","S") #if there is an s in the champion it replaces it with a capital S
        champion = champion.replace("m","M") #if there is an m in the champion it replaces it with a capital M
    else:
        pass

    champion = data[champion] #finds dictionary of data, then champion
    partype = champion["partype"] #finds dictionary of data, then champion, then partype
    return partype

def attackrange(champion):
    """
    The attackrange function returns the attackrange when given the argument of a champion.
    Firstly it deletes any spaces or apostrophes if any are found in the argument,
    then it makes the string lower case and converts the 1st letter into upper case
    then processes the argument and returns the attackrange of a champion
    """
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe

    champion = champion.casefold() #converts string into lower case
    champion = champion.capitalize() #converts 1st letter into upper case

    if champion == 'Reksai' or champion == 'Kogmaw':
        champion = champion.replace("s","S") #if there is an s in the champion it replaces it with a capital S
        champion = champion.replace("m","M") #if there is an m in the champion it replaces it with a capital M
    else:
        pass

    attackrange = data[champion]["stats"]["attackrange"] #finds dictionary of data, then champion, then stats, then attackrange
    return attackrange

def movespeed(champion):
    """
    The movespeed function returns the movespeed when given the argument of a champion.
    Firstly it deletes any spaces or apostrophes if any are found in the argument,
    then it makes the string lower case and converts the 1st letter into upper case
    then processes the argument and returns the movespeed of a champion
    """
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe

    champion = champion.casefold() #converts string into lower case
    champion = champion.capitalize() #converts 1st letter into upper case

    if champion == 'Reksai' or champion == 'Kogmaw':
        champion = champion.replace("s","S") #if there is an s in the champion it replaces it with a capital S
        champion = champion.replace("m","M") #if there is an m in the champion it replaces it with a capital M
    else:
        pass

    movespeed = data[champion]["stats"]["movespeed"] #finds dictionary of data, then champion, then stats, then movespeed
    return movespeed

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
    return message

