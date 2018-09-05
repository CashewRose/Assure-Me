from django.shortcuts import render
from django.template import RequestContext

def initial(request):
    """This function gets the view to the initial.html template and returns it to the requester
    
    Method Arguments:
        request -- The full HTTP request object
        
    Author:
        Cashew Rose
    """

    template_name = 'initial.html'
    return render(request, template_name, {})