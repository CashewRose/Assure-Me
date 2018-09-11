from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


account_sid = 'AC518612d8e9a66805a2572eefa25e5767'
auth_token = 'e086659598367ab0b3fd84225379d8be'
client = Client(account_sid, auth_token)

@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()
    name = request.POST.get('Body', '')

    msg = f'Hey {name}, how are you today?'
    # Add a text message
    msg = resp.message(msg)

    return HttpResponse(str(resp))