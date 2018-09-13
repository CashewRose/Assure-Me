from django.db import models
from django.db.models import *

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """This makes the model setup for the database. It uses the django supplied user model, extends it and makes adjustments to certain properties.
    This User model holds:
        phone_number -- Holds the account specific phone number. Can be left blank or contain up to 10 digits. (String or None)
        confirmed -- Contains a boolean that tells the status of the users phone number. If true they are set up to recieve text messages. (Boolean)
        email -- Holds the users email. Must contain an @ in the input. (String)
        first_name -- Holds the user's first name. Can only be up to 15 characters. (String)
        last_name -- Holds the user's last name. Can only be up to 25 characters. (String)

    Author:
        Cashew Rose
    """

    phone_number = models.CharField(null=True, blank=True, max_length=10)
    confirmed = models.BooleanField(default=False)
    email = models.EmailField(blank=False)
    first_name = models.CharField(blank=False, max_length=15)
    last_name = models.CharField(blank=False, max_length=25)