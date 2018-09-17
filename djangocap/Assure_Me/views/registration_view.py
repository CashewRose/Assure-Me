from django.shortcuts import render
from django.core.exceptions import ValidationError
from Assure_Me.forms import RegisterForm
from .login_logout_view import login_user
from .send_sms import send_sms

def register(request):
    '''Handles the creation of a new user for authentication

    Method Arguments:
        request -- The full HTTP request object

    Author:
        Cashew Rose
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)

        if register_form.is_valid():
            # Save the user's form data to the database.
            user = register_form.save()

            # Checks if the field is empty, otherwise next code would throw an error
            if user.phone_number != None:

                # If the phone number field was input with a valid number and they dont have an active confirmation, it starts the confirmation process
                if len(user.phone_number) == 10 and user.phone_number.isdigit():
                    send_sms(user.phone_number)
             

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            # Update our variable to tell the template registration was successful.
            registered = True
            return login_user(request)

        else: 
            template_name = 'register.html'
            return render(request, template_name, {'register_form': register_form})

    elif request.method == 'GET':
        register_form = RegisterForm()
        template_name = 'register.html'
        return render(request, template_name, {'register_form': register_form})
