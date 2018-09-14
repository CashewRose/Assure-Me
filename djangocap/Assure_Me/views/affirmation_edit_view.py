from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from Assure_Me.models import Affirmation
from django.contrib.auth.decorators import login_required

    
@login_required   
def edit_affirmation_view(request, Affirmation_Id):

    '''Handles editting an affirmation that the user has

    Method arguments:
        request -- The full HTTP request object
        Affirmation_Id -- Affirmation's specific id that is being editted
        
    Author:
        Cashew Rose
    '''

    if request.method == "POST":
        try:
            affirm = Affirmation.objects.get(pk=Affirmation_Id)
            # This makes sure only the owner of the affirmation can actually delete the instance of it
            if request.user.id == affirm.user_id:  

                # Gets the inputs value for the new affirmation changes
                edit_affirmation=request.POST['affirmation']

                # Saves the new affirmation value to the existing instance to make an updated instance
                edit_post = Affirmation(id=Affirmation_Id, affirmation=edit_affirmation, user_id=affirm.user_id)

                # Saves the updated instance to the existing instance in the Affirmation Model
                edit_post.save()

                return redirect('/affirmations')
            
            else: 
                return redirect('/affirmations')

        # Accounts for if there affirmation has already been deleted
        except ObjectDoesNotExist:
            return redirect('/affirmations')

    else: 
        return redirect('/affirmations')
