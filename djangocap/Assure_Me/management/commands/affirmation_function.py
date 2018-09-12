import os

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Assure_Me.models import User, Affirmation

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            affirm_users_to_send = User.objects.filter(confirmed=True)
            print(users_affirmations)
            for user in affirm_users_to_send:
                number = '+1' + user.phone_number
                affirm = Affirmation.objects.filter(user_id=user.id)

                message = client.messages \
                    .create(
                            body=affirm[0].affirmation,
                            from_='+16158662463',
                            to=number
                        )

        except ObjectDoesNotExist:
            print("No one to send messages to today!")



