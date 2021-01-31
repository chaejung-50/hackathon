import json, requests

def getTopAnime():

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={loc.capitalize()}&units=imperial&appid={key}")