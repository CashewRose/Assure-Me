from django.shortcuts import render
from django.template import RequestContext

def initial(request):
    template_name = 'initial.html'
    return render(request, template_name, {})