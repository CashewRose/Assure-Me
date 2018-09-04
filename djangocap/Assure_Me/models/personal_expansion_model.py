from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    phone_number = models.IntegerField(validators=[MinLengthValidator(10), MinLengthValidator(10)], blank=True, null=True)
    confirmed = models.BooleanField(default=False)