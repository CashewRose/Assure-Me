from django.shortcuts import render
from django.contrib.auth.decorators import login_required

 
def account_edit_view(request):
    
    ##Runs only when form is submitted
    if request.method == "POST":
        user_form = EditFormUser(request.POST, instance=request.user)
        customer_form = EditFormCustomer(request.POST, instance=customer_instance)

        ##Checks everything in both forms is filled out correctly and saves them with the new information. Sends them back to the main account page when finished.
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save()

            return redirect('website:account_home')

    else: 
        formCustomer= EditFormCustomer(instance=customer_instance)
        formUser = EditFormUser(instance=request.user)

    ##Displays the page with the forms    
    return render(request, 'account/account_edit.html', {'customer_form': formCustomer,
    'user_form': formUser})