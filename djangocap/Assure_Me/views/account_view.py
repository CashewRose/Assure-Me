from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def account_view(request):
    """This function gets the view to the account.html template and returns it to the requester
    
    Method Arguments:
        request -- The full HTTP request object
        
    Author:
        Cashew Rose
    """

    template = 'account.html'
    return render(request, template)
