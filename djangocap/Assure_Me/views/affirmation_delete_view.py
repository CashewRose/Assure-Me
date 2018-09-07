from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from Assure_Me.models import Affirmation


def delete_affirmation_view(request, Affirmation_Id):
    '''Handles deleting the selected affirmation from the user's collection

    Method arguments:
        request -- The full HTTP request object
        Affirmation_Id -- The id of the affirmation instance being deleted
        
    Author:
        Cashew Rose
    '''
    try:
        affirmation = Affirmation.objects.get(pk=Affirmation_Id)
        affirmation.delete()
        return redirect('/affirmations')

    # Accounts for if there affirmation has already been deleted
    except ObjectDoesNotExist:
        return redirect('/affirmations')
