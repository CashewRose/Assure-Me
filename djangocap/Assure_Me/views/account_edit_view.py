from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Assure_Me.forms import AccountEditForm

 
def account_edit_view(request):

    """This will give the users a form where they can update their account information. On submit it will update their account information and save it to the database. 
    
    Method Arguments:
        request -- The full HTTP request object

    Author: 
        Cashew Rose
    """
    
    ##Runs only when form is submitted
    if request.method == "POST":
        user_form = AccountEditForm(request.POST, instance=request.user)

        ##Checks everything in both forms is filled out correctly and saves them with the new information. Sends them back to the main account page when finished.
        if user_form.is_valid():
            user = user_form.save()

            return redirect('Assure_Me:account')

    else: 
        formUser = AccountEditForm(instance=request.user)

    ##Displays the page with the forms    
    return render(request, 'account_edit.html', {'user_form': formUser})