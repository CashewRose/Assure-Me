import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Assure_Me.models import User
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@csrf_exempt
def sms_response(request):

    """Responds correctly to the users text message. Responses:
        Confirm -- Adds a user as verified and begins the daily text message process.
        Stop! -- Removes a users confirmed status and their phone number from the database.
            (Twilio has auto stop commands that will prevent me from sending and unsubscribing the user if user)
        (Anything inbetween)  -- Will add a response message with command options
    
    Method Arguments:
        request -- The full twilio request object

    Author: 
        Cashew Rose
    """
    # Start our TwiML response
    resp = MessagingResponse()

    # Checks if the user responded to the message with the Confirm message
    if request.POST.get('Body').strip(" ./,0123456789 \" \' ").lower() == 'confirm':
       
        # Compares the numbers we have in the system minus the country code and finds the correct user to change their validation to true
        number = request.POST.get('From', '')[2:]
        user_to_confirm = User.objects.filter(phone_number=number)

        # Checks to make sure it can find at least one otherwise it will error
        if len(user_to_confirm) !=0:
            user_to_confirm = user_to_confirm[0]
            user_to_confirm.confirmed = True
            user_to_confirm.save()

            # Add a text message
            msg = f'Welcome! You have now joined Assure Me. You will begin getting messages starting tomorrow. Be sure and add an affirmation if you haven\'t already.'
            resp.message(msg)

            return HttpResponse(str(resp))

        # If no recognition, they texted the number without registering
        else:

            # Add a text message
            msg = f'It seems we don\'t have your phone number in our system. Please re-enter it on Assure Me and try again.'
            resp.message(msg)

            return HttpResponse(str(resp))

    # Checks to see if the user wants to cancel their subscription with Assure Me   
    elif (request.POST.get('Body').strip(" ./,0123456789! \" \' ").lower()) == 'stop':

        # Compares the numbers we have in the system minus the country code and finds the correct user to change their validation to true
        number = request.POST.get('From', '')[2:]
        user_to_delete = User.objects.filter(phone_number=number)

        # Checks to make sure it can find at least one user with this number otherwise it will error
        if len(user_to_delete) !=0:
            user_to_delete = user_to_delete[0]
            user_to_delete.confirmed = False
            user_to_delete.phone_number = None
            user_to_delete.save()

            # Add a text message
            msg = f'We are sorry to see you go. If you would like to rejoin our subscription at anytime, please re-enter your number on Assure Me.'
            resp.message(msg)

            return HttpResponse(str(resp))

        # The user is already removed or never registered with Assure Me
        else:
            # Add a text message
            msg = f'You are not currently subscribed with us. If you would like to rejoin our subscription at anytime, please re-enter your number on Assure Me.'
            resp.message(msg)

            return HttpResponse(str(resp))

    # If the user messages the application with anything else they will get a response message with available commands
    else:
        # Add a text message
        msg = f'I\'m sorry I don\'t understand. You can respond with \'Stop!\' to unsubscribe from Assure Me. Or \'Confirm\' if you haven\'t finished your validation.'
        resp.message(msg)

        return HttpResponse(str(resp))

