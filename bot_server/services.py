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
        "attackRange": [str],
}

def title(champion):
#returns the title of the champion
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe
    if champion == 'RekSai' or champion == 'KogMaw':
        pass
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        champion = champion.casefold() #converts string into lower case
        champion = champion.capitalize() #converts 1st letter into upper case

    champion = data[champion] #finds dictionary of champion inside data
    title = champion["title"] #finds dictionary of title inside champion
    return title

def blurb(champion):
#returns the blurb of a champion
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe
    if champion == 'RekSai' or champion == 'KogMaw':
        pass
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        champion = champion.casefold() #converts string into lower case
        champion = champion.capitalize() #converts 1st letter into upper case

    champion = data[champion] #finds dictionary of champion inside data
    blurb = champion["blurb"] #finds dictionary of blurb inside champion
    return blurb

def partype(champion):
#returns the partype (what casting resource the champion)
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe
    if champion == 'RekSai' or champion == 'KogMaw':
        pass
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        champion = champion.casefold() #converts string into lower case
        champion = champion.capitalize() #converts 1st letter into upper case

    champion = data[champion] #finds dictionary of data, then champion
    partype = champion["partype"] #finds dictionary of data, then champion, then partype
    return partype

def attackrange(champion):
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe
    if champion == 'Reksai' or champion == 'Kogmaw':
        pass
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        champion = champion.casefold() #converts string into lower case
        champion = champion.capitalize() #converts 1st letter into upper case

    attackrange = data[champion]["stats"]["attackrange"] #finds dictionary of data, then champion, then stats, then attackrange
    return attackrange

def movespeed(champion):
    address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
    r = requests.get(address)
    r_json = r.json()
    data = r_json['data']

    champion = champion.replace(" ","")  #replaces spaces so no edge case there
    if champion.find("'")>= 0: #champions such as Kha'zix, Vel'koz, Cho'gath etc are sometimes spelled with an apostrophe
        champion = champion.replace("'","")  #deletes the apostrophe
    if champion == 'RekSai' or champion == 'KogMaw':
        pass
    #nothing happens because I don't know how to generalize code for something with captial letter in the middle
    #RekSai & KogMaw are literally the only champions with a captial letter in the middle (2/152 champions)
    else: #for literally every champion aside from RekSai & KogMaw
        champion = champion.casefold() #converts string into lower case
        champion = champion.capitalize() #converts 1st letter into upper case

    movespeed = data[champion]["stats"]["movespeed"] #finds dictionary of data, then champion, then stats, then movespeed
    return movespeed
# print(title("Zed"))
# print(blurb("Zed"))
# print(partype("Zed"))

# something like

# r = requests.get(address)
# r_json = r.json()
# data = r_json['data']
# aatrox = data["Aatrox"]
# blurb = aatrox["blurb"]
