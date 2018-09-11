from twilio.rest import Client

def send_sms(num):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC518612d8e9a66805a2572eefa25e5767'
    auth_token = 'e086659598367ab0b3fd84225379d8be'
    client = Client(account_sid, auth_token)

    number = '+1' + num
    message = client.messages \
        .create(
                body="Welcome to Assure Me! If you would like to confirm your registration to this number, reply with 'Confirm'",
                from_='+16158662463',
                to=number
            )

    print(message.sid)