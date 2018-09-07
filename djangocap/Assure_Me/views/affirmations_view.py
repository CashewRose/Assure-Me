from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from Assure_Me.models import Affirmation

@login_required
def affirmations_view(request):
    """This function gets the view to the affirmations.html template and returns it to the requester.
        It filters and grabs all of the sepcific users affirmations and sends that to the template accordingly.
    
    Method Arguments:
        request -- The full HTTP request object
        
    Author:
        Cashew Rose
    """

    try:
        affirmations = Affirmation.objects.filter(user=request.user.id)
        print(affirmations)
        return render(request, "affirmations.html", {'affirmations': affirmations})

    # Accounts for if there are no current affirmations for that user
    except ObjectDoesNotExist:
        return render(request, "affirmations.html")