from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from Assure_Me.models import Affirmation

@login_required
def affirmations_view(request):

    affirmations = get_list_or_404(Affirmation, user=request.user.id)
    print(affirmations)
    return render(request, "affirmations.html", {'affirmations': affirmations})