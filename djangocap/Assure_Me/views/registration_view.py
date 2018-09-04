from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from 


def register(request):
    '''Handles the creation of a new user for authentication

    Method Arguments:
        request -- The full HTTP request object

    Author:
        Cashew Rose
    '''

#     # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

#     # Create a new user by invoking the `create_user` helper method
#     # on Django's built-in User model
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = register_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        register_form = RegisterForm()
        template_name = 'register.html'
        return render(request, template_name, {'register_form': register_form)
