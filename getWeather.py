import requests
import json

def api_response(loc):
#loc = input("Where are you from?\n").lower()

    key = "bf3c1639ec81c85a49257898b778d0d2"

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={loc.capitalize()}&units=imperial&appid={key}")

    if (response.status_code == 404):
        return "ERROR IN CONNECTIONS"
    else:
        temp_curr = response.json()['main']['temp']
        temp_max = response.json()['main']['temp_max']
        temp_min = response.json()['main']['temp_min']
        feels = response.json()['main']['feels_like']
        weather = response.json()['weather'][0]['description']

        if (feels < 67):
            if ("clouds" in weather):
                return f"It's {temp_curr} degress and {weather} outside. It's pretty chilly, might want to wear a jacket!"
            else:
                return f"It's {temp_curr} degress outside. You might want to wear something warm now!"
        else:
            if ("clouds" in weather and temp_min < 65):
                return f"It's {temp_curr} degress outside. There are some clouds, might want to bring a jacket for later!"
            else:
                return f"It's {temp_curr} degress outside. It's warm today!"