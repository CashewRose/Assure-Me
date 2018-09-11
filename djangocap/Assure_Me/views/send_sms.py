import os

from twilio.rest import Client


def send_sms(num):
    """This sends an initial text message to start and setup the user for Assure Me.
    
    Method Arguments:
        num -- takes a client entered phone number as an argument to send the text message destination correctly

    Author: 
        Cashew Rose
    """
    # Account Sid and Auth Token from twilio.com/console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    # Adjusts the number to be in correct twilio format before being plugged in
    number = '+1' + num

    message = client.messages \
        .create(
                body="Welcome to Assure Me! If you would like to confirm your registration to this number, reply with 'Confirm'",
                from_='+16158662463',
                to=number
            )

    print(message.sid)