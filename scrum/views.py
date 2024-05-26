from django.shortcuts import render, redirect
from .models import Scrum, Feature, Review
from .forms import ContactForm
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail, EmailMessage

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


def Contact_Me(request):
    """
    A view for all users to send a message.
    """
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = contactForm.cleaned_data['name']
            email = contactForm.cleaned_data['email']
            message = contactForm.cleaned_data['message']
            
            new_email = EmailMessage(
                subject=f"New Message from {name}",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=["ananikolayenia@gmail.com"],
                reply_to=[email]
            )
            new_email.send()

            messages.add_message(
                request, messages.SUCCESS, '''Your message has been sent! 
                We endeavour to respond within 2 business days :)'''
            )
            return redirect('hello')
    else:
        contactForm = ContactForm()
    context = {
        'contactForm' : contactForm,
    }
    return render(
        request, 
        "scrum/contact.html",
        context
    )