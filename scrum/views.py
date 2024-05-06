from django.shortcuts import render
from .models import Scrum, Feature, Review

def HelloScrum(request):
    scrum = Scrum.objects.all().first()
    feature = Feature.objects.all()
    all_reviews = Review.objects.all()
    five_stars = Review.objects.filter(rating='★★★★★')
    four_stars = Review.objects.filter(rating='★★★★☆')
    context = {
        'hello' : scrum,
        'feature' : feature,
        'all_reviews': all_reviews,
        'five_star': five_stars,
        'four_star': four_stars,
        }
    
    return render(
        request,
        "scrum/index.html",
        context
    )