from django.shortcuts import render
from .models import Scrum

def HelloScrum(request):
    scrum = Scrum.objects.all()
    context = {'hello' : scrum}
    
    return render(
        request,
    "scrum/index.html",
    context
    )