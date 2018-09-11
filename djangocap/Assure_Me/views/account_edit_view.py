from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .send_sms import send_sms
from Assure_Me.forms import AccountEditForm
from Assure_Me.models import User

@login_required
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

        ##Checks everything in forms is filled out correctly and saves them with the new information. Sends them back to the main account page when finished.
        if user_form.is_valid():

            user_form.changed_data
            print(user_form.cleaned_data.get('phone_number'))
            print(user_form.changed_data)
            user = user_form.save()
            if 'phone_number' in user_form.changed_data:
                print(user.pk)
                paste = User.objects.get(pk=user.pk)
                paste.confirmed = True
                paste.save()

                paste.save()
                if len(user.phone_number) == 10 and user.phone_number.isdigit() and user.confirmed == False:
                    paste = User(confirmed=True, pk=user.pk)
                    send_sms(user.phone_number)
                    paste.save()

                elif user.confirmed == True:
                    user.confirmed


            return redirect('Assure_Me:account')

    else: 
        formUser = AccountEditForm(instance=request.user)

    ##Displays the page with the form    
    return render(request, 'account_edit.html', {'user_form': formUser})