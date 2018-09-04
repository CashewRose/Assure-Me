# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.shortcuts import render
# from django.template import RequestContext
# from website.forms import UserForm, CustomerForm


# def register(request):
#     '''Handles the creation of a new user for authentication

#     Method arguments:
#     request -- The full HTTP request object
#     '''

#     # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
#     registered = False

#     # Create a new user by invoking the `create_user` helper method
#     # on Django's built-in User model
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         customer_form = CustomerForm(data=request.POST)

#         if user_form.is_valid() and customer_form.is_valid():
#             # Save the user's form data to the database.
#             user = user_form.save()
#             customer = customer_form.save(commit=False)
#             customer.user = user
#             customer.save()

#             # Now we hash the password with the set_password method.
#             # Once hashed, we can update the user object.
#             user.set_password(user.password)
#             user.save()

#             # Update our variable to tell the template registration was successful.
#             registered = True

#         return login_user(request)

#     elif request.method == 'GET':
#         user_form = UserForm()
#         customer_form = CustomerForm()
#         template_name = 'register.html'
#         return render(request, template_name, {'user_form': user_form, 'customer_form': customer_form})
