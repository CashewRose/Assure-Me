import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    print(request.POST.get('Body').lower())
    if request.POST.get('Body').lower() == 'confirm':
        print('yup')
        
    name = request.POST.get('Body', '')

    msg = f'Hey {name}, how are you today?'
    
    # Add a text message
    msg = resp.message(msg)

    return HttpResponse(str(resp))