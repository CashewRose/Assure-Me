from django.shortcuts import render
from django.http import HttpResponseRedirect

def csrf_failure(request):

    # Accounts for the error that occurs is the user tries to go back in their browser
    # Redirects them according to their login status
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/')