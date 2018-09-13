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

    """Responds correctly to the users text message.
    
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

        if len(user_to_confirm) !=0:
            user_to_confirm = user_to_confirm[0]
            user_to_confirm.confirmed = True
            user_to_confirm.save()

            # Add a text message
            msg = f'Welcome! You have now joined Assure Me. You will begin getting messages starting tomorrow. Be sure and add an affirmation if you haven\'t already.'
            resp.message(msg)

            return HttpResponse(str(resp))

        else:

            # Add a text message
            msg = f'It seems we don\'t have your phone number in our system. Please re-enter it on Assure Me and try again.'
            resp.message(msg)

            return HttpResponse(str(resp))
        
    elif request.POST.get('Body').strip(" ./,0123456789! \" \' ").lower() == 'stop':

        # Compares the numbers we have in the system minus the country code and finds the correct user to change their validation to true
        number = request.POST.get('From', '')[2:]
        user_to_delete = User.objects.filter(phone_number=number)
        user_to_delete = user_to_delete[0]
        user_to_delete.confirmed = False
        user_to_delete.phone_number = None
        user_to_delete.save()

        # Add a text message
        msg = f'We are sorry to see you go. If you would like to rejoin our subscription at anytime, please re-enter your number on Assure Me.'
        resp.message(msg)

        return HttpResponse(str(resp))