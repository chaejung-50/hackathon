from twilio.rest import Client
import credentials
import random 
import schedule
import getJokes
import time
import getJokes

Morning_Stuff = ["i love you biiiiitch, i ain't never gonna stop loving you biiiiiitch", 
                 "Morning beautiful",
                "Wake up bihhh"]
account_sid = credentials.account_sid
auth_token = credentials.auth_token
client = Client(account_sid, auth_token)

def send_mess(quote):
    global client
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=quote)


quote = Morning_Stuff[random.randint(0, len(Morning_Stuff))]
schedule.every().day.at("20:15").do(send_mess, Morning_Stuff[0])
schedule.every().hour.do(getJokes.sendJokes())

while True:
    schedule.run_pending()
    time.sleep(2)
