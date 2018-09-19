from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect

def initial(request):
    """This function gets the view to the initial.html template and returns it to the requester
    
    Method Arguments:
        request -- The full HTTP request object
        
    Author:
        Cashew Rose
    """

    # Only allows access to this page if the user is logged out, otherwise directs them to their personal home page
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    else:
        template_name = 'initial.html'
        return render(request, template_name, {})