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
    if request.POST.get('Body').strip(" ./,0123456789 \" \' ").lower() == 'confirm':
        number = request.POST.get('From', '')[2:]
        user_to_confirm = User.objects.filter(phone_number=number)
        user_to_confirm = user_to_confirm[0]
        user_to_confirm.confirmed = True
        user_to_confirm.save()
        msg = f'Welcome!'

        # Add a text message
        resp.message(msg)

        return HttpResponse(str(resp))