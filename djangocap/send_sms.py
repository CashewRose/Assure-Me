from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC518612d8e9a66805a2572eefa25e5767'
auth_token = 'e086659598367ab0b3fd84225379d8be'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
            body="Hi it's Cashew! I'm sending this message because it\'s a mini accomplishment. This text was sent through my python django app! L33t right? <3 (PS, text the app back for a cute owl!)",
            from_='+16158662463',
            to='+16159670606'
        )

print(message.sid)