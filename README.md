# The Perfect Assistant
## Inspiration
At first, we had no idea how to start with the Twilio API and it’s various applications. After much research, we found that Twilio had its own conversation API, but unfortunately, it was still under beta testing and we had no access to this. Since we saw the possibility of the Twilio API, we wanted to try creating our own personal assistant using a combination of multiple different APIs.

Although our current assistant is only a proof-of-concept, there is much potential for AI bots to offer support in everyday life and provide a direct and easy way to get information whenever you need it.

## What it does
The Perfect Assistant is a Python app that connects our virtual assistance Bot with our users! You can have a friend to keep you company and answer questions you may have about anything!

## How we built it
Our application is built using the Twilio and Wolfram APIs that allow our users to converse with a Bot that is fully capable of helping and answering our users questions. We utilized a Weather API, Compliment API, and Joke API to add some functionality to our Bot. The Wolfram API covered many of the conversational areas we couldn’t program ourselves.

## Challenges we ran into
At first, we had a difficult time connecting with the Twilio API and triggering the correct responses from our bot, but after taking another look at the documentation, our answer smacked us in the face. Implementing the various APIs to get information for the bot to send back was easy enough, but we wanted our bot to be able to converse with our users. At first, we tried training and building a model for a chat bot, but our labels did not seem to work and the bot only replied with greetings (training code is still in the repository).

## What we learned
We learned a lot about API calls and establishing the correct connections between the program and its destination. While working towards a conversation bot, we learned a lot about ML/AI in training our model.

## What's next for The Perfect Partner
In the future, we would love to add video and voice input with recognition and potentially make this into a mobile application that can support more and more users. We would love to develop our own ML/AI ChatBot that could be trained to be better than the Wolfram API. At first, we hoped to develop a more health based, Chat bot, so we hope to incorporate that vision in the future and develop a therapy bot feature where a user can get some advice or be connected with a therapist.

## How to run
`python receive_sms.py`

`python send_sms.py`
