import os
import random

from django.core.management.base import BaseCommand

from Assure_Me.models import User, Affirmation

from twilio.rest import Client

# Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class Command(BaseCommand):

    def handle(self, *args, **options):

        affirm_users_to_send = User.objects.filter(confirmed=True)
        if len(affirm_users_to_send) !=0:
            for user in affirm_users_to_send:
                number = '+1' + user.phone_number
                affirm = Affirmation.objects.filter(user_id=user.id)

            if len(affirm) != 0:
                message = client.messages \
                    .create(
                            body=random.choice(affirm).affirmation,
                            from_='+16158662463',
                            to=number
                        )
            else:
                print("This user hasn't put in any affirmations yet!")
        else:
            print("No users to send messages to today!")
                        
