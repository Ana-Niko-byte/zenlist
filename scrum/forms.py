from django import forms

class ContactForm(forms.Form):
    """
    A form for all users to contact the site owner with a message.
    """
    name = forms.CharField(label='Your Name')
    email = forms.EmailField()
    message = forms.CharField(max_length=200, widget=forms.Textarea)
