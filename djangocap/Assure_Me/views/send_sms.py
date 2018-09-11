from twilio.rest import Client
import os

print(os.environ)

def send_sms(num):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    number = '+1' + num
    message = client.messages \
        .create(
                body="Welcome to Assure Me! If you would like to confirm your registration to this number, reply with 'Confirm'",
                from_='+16158662463',
                to=number
            )

    print(message.sid)