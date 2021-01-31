from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import getWeather, getJokes, getCompliment, myNamDoSan
# from Bot import SimpleChat


app = Flask(__name__)
weatherflag = 0
botflag = 0

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    global weatherflag
    # global botflag
	# Get the message the user sent to Twilio number
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if weatherflag == 1:
        weather = getWeather.api_response(body)
        resp.message(weather)
        weatherflag = 0
    #
    # elif botflag == 1:
    #     bot = SimpleChat.bot_message(body)
    #     resp.message(bot)
    #     if "stop" in body:
    #         botflag=0

    elif 'weather' in body.lower():
        resp.message("Where are you From?")
        weatherflag=1

    elif 'joke' in body.lower():
        joke = getJokes.getJoke()
        resp.message(joke["setup"])
        resp.message(joke["punchline"])

    elif 'compliment' in body.lower() or ("say" in body.lower() and "nice" in body.lower() and "something" in body.lower()):
        compliment = getCompliment.giveCompliment()
        resp.message(compliment)

    elif body == 'bye':
        resp.message("Goodbye")

    elif 'bot' in body.lower():
        resp.message("Hi! I'm your friendly AI, Nam Do San!")
        # botflag = 1
    else:
        print('exist')
        resp.message(myNamDoSan.api_response(body))

    return str(resp)
 
if __name__ == "__main__":
  app.run(debug=True)

  
