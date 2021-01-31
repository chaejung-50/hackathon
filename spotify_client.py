import random
import string
import urllib
import requests

class SpotifyClient(object):
    def __init__(self, api_key):
        self.api_key = api_key
        print(api_key)

    def get_random_tracks(self):
        # %char%
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'

        response = requests.get(url,
                                headers={
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {self.api_key}"
                                })

        response_json = response.json()
        print(response_json)
        #tracks = [track for track in response_json['tracks']['items']]
        return response_json
