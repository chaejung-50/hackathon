from twilio.rest import Client
import requests
import json
import credentials
import time

account_sid = credentials.account_sid
auth_token = credentials.auth_token
client = Client(account_sid, auth_token)

def getJoke():
    url = "https://official-joke-api.appspot.com/random_joke"
    data = requests.get(url)
    tt = json.loads(data.text)
    return tt

def tellJokes():
    global client
    joke = getJoke()
    setup = joke["setup"]
    punchline = joke["punchline"]
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body="uh... tell you a joke? hm...")
    time.sleep(4)
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=setup)
    time.sleep(2)
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=punchline)

def sendJokes():
    global client
    joke = getJoke()
    setup = joke["setup"]
    punchline = joke["punchline"]
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body="hellooo! Do you want to hear a joke? :3")
    time.sleep(3)
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body="ok well i don't care if you want to or not but")
    time.sleep(4)
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=setup)
    time.sleep(2)
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=punchline)

