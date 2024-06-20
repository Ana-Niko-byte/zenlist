from django import forms
from .models import Review


class ContactForm(forms.Form):
    """
    A form for all users to contact the site owner with a message.
    """
    # Adding placeholders:
    # https://stackoverflow.com/questions/4101258/
    # how-do-i-add-a-placeholder-on-a-charfield-in-django
    name = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'John Smith'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'john.smith@example.com'}
        )
    )
    message = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={'placeholder': 'I love Zenlist...'}
        ),
        label='Message (max 200 characters)'
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('job_industry', 'rating', 'review',)
        labels = {
            'job_industry' : 'Your Industry',
            'rating' : 'How did we do?',
            'review' : 'Share Your Thoughts (max 120 characters)'
        }
