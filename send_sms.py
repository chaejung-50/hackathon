from twilio.rest import Client
import random 
import schedule
import time
import getJokes
import credentials

Morning_Stuff = ["Good morning beautiful :)",
                 "I love waking up and knowing I get to see you today.",
                "I had the sweetest dream about you last night.",
                 "Knowing you’re in my life makes every morning so much better."]
account_sid = credentials.account_sid
auth_token = credentials.auth_token
client = Client(account_sid, auth_token)

def send_mess(quote):
    global client
    client.messages.create(
        to = credentials.my_cell,
        from_= credentials.my_twilio,
        body=quote)


quote = Morning_Stuff[random.randint(0, len(Morning_Stuff)-1)]
client = Client(account_sid, auth_token)
client.messages.create(
    to = credentials.my_cell,
	from_= credentials.my_twilio,
    body= quote)


schedule.every().day.at("20:15").do(send_mess, Morning_Stuff[0])
schedule.every().hour.do(getJokes.sendJokes)

while True:
    schedule.run_pending()
    time.sleep(2)
