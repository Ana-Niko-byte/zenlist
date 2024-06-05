from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Scrum, Review
from .forms import ContactForm, ReviewForm
from django.contrib import messages

from django.conf import settings
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required

def HelloScrum(request):
    scrum = Scrum.objects.all().first()
    all_reviews = Review.objects.all()
    five_stars = Review.objects.filter(rating='★★★★★')
    four_stars = Review.objects.filter(rating='★★★★☆')
    if request.method == 'POST':
        reviewForm = ReviewForm(data=request.POST)
        if reviewForm.is_valid:
            review = reviewForm.save(commit=False)
            review.author = request.user
            review.approved = False
            reviewForm.save()
            messages.add_message(
                request, messages.SUCCESS,
                '''Thanks for your review! Our administrators will 
                review your submission within 2 business days.'''
            )
            return redirect('hello')
        else:
            messages.add_message(
            request, messages.SUCCESS,
            '''There was an issue while trying to submit your review. 
            Please try again in a few mins. 
            If the issue persists, please contact us using our dedicated 
            contact page.'''
        )
    else:
        reviewForm = ReviewForm()

    context = {
        'hello' : scrum,
        'all_reviews': all_reviews,
        'five_star': five_stars,
        'four_star': four_stars,
        'reviewForm': reviewForm,
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

def Zenlist_Reviews(request):
    all_reviews = Review.objects.all()
    best_reviews = Review.objects.filter(rating__icontains='★★★')
    five_star = Review.objects.filter(rating='★★★★★')
    four_star = Review.objects.filter(rating='★★★★☆')
    three_star = Review.objects.filter(rating='★★★☆☆')
    two_star = Review.objects.filter(rating='★★☆☆☆')
    one_star = Review.objects.filter(rating='★☆☆☆☆')
    user_reviews = Review.objects.filter(author=request.user, approved=False)

    if request.method == 'POST':
        reviewForm = ReviewForm(data=request.POST)
        if reviewForm.is_valid:
            review = reviewForm.save(commit=False)
            review.author = request.user
            review.approved = False
            reviewForm.save()
            messages.add_message(
                request, messages.SUCCESS,
                '''Thanks for your review! Our administrators will 
                review your submission within 2 business days.'''
            )
            return redirect('hello')
        else:
            messages.add_message(
            request, messages.SUCCESS,
            '''There was an issue while trying to submit your review. 
            Please try again in a few mins. 
            If the issue persists, please contact us using our dedicated 
            contact page.'''
        )
    else:
        reviewForm = ReviewForm()

        context = {
        'reviews': all_reviews,
        'one_star': one_star,
        'two_star': two_star,
        'three_star': three_star,
        'four_star': four_star,
        'five_star': five_star,
        'user_reviews': user_reviews,
        'best_reviews': best_reviews,
        'reviewForm': reviewForm,
    }

    return render(
        request,
        "scrum/reviews.html",
        context
    )

@login_required
def delete_review(request, id):
    """
    FBV for deleting a review based on id retrieval.
    """
    review = get_object_or_404(Review, id=id)
    if review.author == request.user:
        review.delete()
        return HttpResponseRedirect(reverse('reviews'))