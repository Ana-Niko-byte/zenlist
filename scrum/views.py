from django.shortcuts import render
from .models import Scrum, Feature, Review

def HelloScrum(request):
    scrum = Scrum.objects.all().first()
    # Queryset was being returned from 3 to 1.
    features = Feature.objects.all()
    all_reviews = Review.objects.all()
    five_stars = Review.objects.filter(rating='★★★★★')
    four_stars = Review.objects.filter(rating='★★★★☆')

    # Queryset was being returned from 3 to 1.   
    def reversed_features(features):
        reversed_features = []
        for feature in features:
            reversed_features.append(feature)
        reversed_features.reverse()
        return reversed_features

    reversed_features = reversed_features(features)

    context = {
        'hello' : scrum,
        'features' : features,
        'reversed_features' : reversed_features,
        'all_reviews': all_reviews,
        'five_star': five_stars,
        'four_star': four_stars,
        }
    
    return render(
        request,
        "scrum/index.html",
        context
    )