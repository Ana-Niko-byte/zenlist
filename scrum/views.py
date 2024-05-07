from django.shortcuts import render
from .models import Scrum, Feature, Review

def HelloScrum(request):
    scrum = Scrum.objects.all().first()
    features = Feature.objects.all()
    all_reviews = Review.objects.all()
    five_stars = Review.objects.filter(rating='★★★★★')
    four_stars = Review.objects.filter(rating='★★★★☆')

    def combined_ids(self):
        list1 = ['list-item-1', 'list-item-2', 'list-item-3']
        list2 = self.features
        combined_lists = zip(list1, list2)
        return {'combined_lists': combined_lists}

    context = {
        'hello' : scrum,
        'features' : features,
        'all_reviews': all_reviews,
        'five_star': five_stars,
        'four_star': four_stars,
        }
    
    return render(
        request,
        "scrum/index.html",
        context
    )