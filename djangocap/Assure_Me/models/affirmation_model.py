from django.db import models
from django.db.models import *

class Affirmation(models.Model):
    """This makes the model setup for the database. 
    This Affirmation model holds:
        user -- Which connects the affirmations they make to their specific account id. (FK)
        affirmation -- Holds one of the specific affirmations written by the user. (String)
      
    Author:
        Cashew Rose
    """
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
    )
    affirmation = models.CharField(max_length=500)