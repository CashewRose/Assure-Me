from django.db import models
from django.db.models import *

class Affirmation(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    affirmation = models.CharField(max_length=500)