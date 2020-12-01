# service.py
# This file should contain the functions used to run your service.
#
# Author: Wesley Chui
import requests
# service provided and expected arguments
services_dict = {
        "partype": [str],
        "blurb": [str],
        "tag": [str],
}

def partype(champion):
#returns the partype (what casting resource the champion)
address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
r = requests.get(address)
r_json = r.json()
data = r_json['data']
#champion = {}
champion = data[champion]
partype = champion["partype"]

def blurb(champion):
#returns the blurb of a champion
address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
r = requests.get(address)
r_json = r.json()
data = r_json['data']
#champion = {}
champion = data[champion]
blurb = champion["blurb"]

def title(champion):
#returns the tag (or tags) of the champion
address = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json'
r = requests.get(address)
r_json = r.json()
data = r_json['data']
#champion = {}
champion = data[champion]
title = champion["title"]


something like

something like
r = requests.get(address)
r_json = r.json()
data = r_json['data']
aatrox = data["Aatrox"]
blurb = aatrox["blurb"]
