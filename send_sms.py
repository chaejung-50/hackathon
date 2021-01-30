from twilio.rest import Client
import credentials

account_sid = credentials.account_sid
auth_token = credentials.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = credentials.my_cell,
    from_= credentials.my_twilio,
    body="i love you biiiiitch, i ain't never gonna stop loving you biiiiiitch")

print(message.sid)
