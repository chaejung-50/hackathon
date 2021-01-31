import json
import requests

def giveCompliment():
    response = requests.get("https://complimentr.com/api")
    return response.json()['compliment']

