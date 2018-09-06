from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator

class User(AbstractUser):
    phone_number = models.CharField(null=True, blank=True, max_length=10)
    confirmed = models.BooleanField(default=False)
    email = models.EmailField(blank=False)
    first_name = models.CharField(blank=False, max_length=15)
    last_name = models.CharField(blank=False, max_length=25)