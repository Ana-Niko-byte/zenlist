from django.shortcuts import render
from .models import Scrum, Feature

def HelloScrum(request):
    scrum = Scrum.objects.all().first()
    feature = Feature.objects.all()
    context = {
        'hello' : scrum,
        'feature' : feature,
        }
    
    return render(
        request,
    "scrum/index.html",
    context
    )