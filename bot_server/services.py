# service.py
# This file should contain the functions used to run your service.
#
# Author: Wesley Chui
import requests
# service provided and expected arguments
services_dict = {
        "partype": [str],
        "blurb": [str],
        "title": [str],
}

def title(champion):
#returns the title of the champion
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    data.replace(" ","")  #replaces spaces so no edge case there
    if data.index("'")>= 0 #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        data.replace("'","")  #deletes the apostrophe
    if data = 'RekSai' or 'KogMaw'
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        data.casefold() #converts string into lower case
        data.capitalize() #converts 1st letter into upper case

    champion = data[champion]
    title = champion["title"]
    return title

def blurb(champion):
#returns the blurb of a champion
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']
    #champion = {}
    champion = data[champion]
    blurb = champion["blurb"]
    return blurb

def partype(champion):
#returns the partype (what casting resource the champion)
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']
    #champion = {}
    champion = data[champion]
    partype = champion["partype"]
    return partype




# print(title("Zed"))
# print(blurb("Zed"))
# print(partype("Zed"))

# something like

# r = requests.get(address)
# r_json = r.json()
# data = r_json['data']
# aatrox = data["Aatrox"]
# blurb = aatrox["blurb"]
