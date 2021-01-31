import credentials
import random
import spotify_client
from spotify_client import SpotifyClient

def run():
    #search spotify for random songs
    spotify_client = SpotifyClient(credentials.client_id)

    #get random song from list and send it to user
    random_tracks = spotify_client.get_random_tracks()
    #tracks = [track['name'] for track in random_tracks]
    #print(tracks)
    #return tracks[random.randint(0, len(tracks)-1)]

if __name__ == "__main__":
    run()
