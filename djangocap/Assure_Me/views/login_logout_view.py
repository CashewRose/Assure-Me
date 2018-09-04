# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.shortcuts import render
# from django.template import RequestContext
# from website.forms import UserForm, CustomerForm


# def login_user(request):
#     '''Handles the creation of a new user for authentication

#     Method arguments:
#     request -- The full HTTP request object
#     '''

#     # Obtain the context for the user's request.
#     context = RequestContext(request)

#     # Stores the path the users were trying to get to originally if its different or takes them to the home screen
#     next = request.GET.get('next') or '/'
#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':

#         # Use the built-in authenticate method to verify
#         username=request.POST['username']
#         password=request.POST['password']
#         authenticated_user = authenticate(username=username, password=password)

#         # If authentication was successful, log the user in
#         if authenticated_user is not None:
#             login(request=request, user=authenticated_user)
#             return HttpResponseRedirect(request.POST.get('next'))

#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print("Invalid login details: {}, {}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")
#     else:
#             #Renders the page via the login.html template and stores the next variable
#             return render(request, 'login.html', {'next': next})

# # Use the login_required() decorator to ensure only those logged in can access the view.
# @login_required
# def user_logout(request):
#     # Since we know the user is logged in, we can now just log them out.
#     logout(request)

#     # Take the user back to the homepage. Is there a way to not hard code
#     # in the URL in redirects?????
#     return HttpResponseRedirect('/')