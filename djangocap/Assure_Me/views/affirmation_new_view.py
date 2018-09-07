from django.http import HttpResponseRedirect
from Assure_Me.models import Affirmation

def new_affirmation_view(request):
    '''Handles adding the new affirmation to the user

    Method arguments:
        request -- The full HTTP request object
        
    Author:
        Cashew Rose
    '''

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        user=request.user.id
        new_affirmation=request.POST['New_Affirmation'] 

        # Creates the new instance and sets it to a variable
        affirm = Affirmation(affirmation=new_affirmation, user_id=user)

        # Saves the instance to the database
        affirm.save()

    # Once new affirmation is saved to the database
    # The path is directed back to the affirmation page to reflect the update
    return HttpResponseRedirect('/affirmations')