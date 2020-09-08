# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from credential import account_sid,auth_token,my_cell,my_twilio


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello Hetal , How are you ? Today Maheta sir will not take your classes",
                     from_=my_twilio,
                     to=my_cell
                 )

print(message.sid)
