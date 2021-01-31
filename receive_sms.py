from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
	# Get the message the user sent to Twilio number
  body = request.values.get('Body', None)

  resp = MessagingResponse()

  if body == 'hi I need attention':
  	resp.message("I'm giving you attention... what do you want")
  else if body == "hehe I'm kidding xD":
  	resp.message("you needy person smh")
  
  return str(resp)
 
if __name__ == "__main__":
  app.run(debug=True)

  
