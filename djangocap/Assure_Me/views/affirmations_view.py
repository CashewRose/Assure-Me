from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from Assure_Me.models import Affirmation

@login_required
def affirmations_view(request):

    try:
        affirmations = Affirmation.objects.filter(user=request.user.id)
        print(affirmations)
        return render(request, "affirmations.html", {'affirmations': affirmations})
        
    except ObjectDoesNotExist:
        return render(request, "affirmations.html")