from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import getWeather

app = Flask(__name__)
weatherflag = 0
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    global weatherflag
	# Get the message the user sent to Twilio number
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if weatherflag == 1:
        weather = getWeather.api_response(body)
        resp.message(weather)
        weatherflag = 0

    elif 'weather' in body.lower():
        resp.message("Where are you From?")
        weatherflag=1

    elif body == 'bye':
        resp.message("Goodbye")

  
    return str(resp)
 
if __name__ == "__main__":
  app.run(debug=True)

  
