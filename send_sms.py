from twilio.rest import Client
import random 
import schedule
import time
import getJokes
import credentials

Morning_Stuff = ["i love you biiiiitch, i ain't never gonna stop loving you biiiiiitch", 
                 "Morning beautiful",
                "Wake up bihhh"]
account_sid = "AC28e1ee7c89b06cbe3d753e5790a411d7"
auth_token = "edf2f4660d6732ab4ffa4125ff5cf927"
client = Client(account_sid, auth_token)

def send_mess(quote):
    global client
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=quote)


client = Client(account_sid, auth_token)
client.messages.create(
    to = credentials.my_cell,
	from_= credentials.my_twilio,
    body="sup bro-ski")

quote = Morning_Stuff[random.randint(0, len(Morning_Stuff)-1)]
schedule.every().day.at("20:15").do(send_mess, Morning_Stuff[0])
schedule.every().hour.do(getJokes.sendJokes)

while True:
    schedule.run_pending()
    time.sleep(2)
