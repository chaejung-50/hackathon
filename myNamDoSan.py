import requests
import json
import credentials


def api_response(query):
    response = requests.get(f"http://api.wolframalpha.com/v1/conversation.jsp?appid={credentials.my_wolfram}&i={query}")

    if (response.status_code == 404):
        return "ERROR IN CONNECTIONS"
    else:
        return (response.json()['result'])
