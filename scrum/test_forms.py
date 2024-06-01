from django.test import TestCase
from .forms import *


class TestContactForm(TestCase):
    '''
    A class for testing the contact form associated with 
    the Scrum model form and if specific user inputs are 
    correctly placed in the form fields.

    Methods:
    test_name_required():
    This test verifies that a populated contact form which is missing a 
    name input is not submitted, and that the error stems from the missing
    name field input. 

    test_email_required():
    This test verifies that a populated contact form which is missing an 
    email input is not submitted, and that the error stems from the missing
    email field input. 

    test_email_correct_format():
    This test verifies that a completed populated contact form is not submitted
    unless the email adheres to the expected email format, and that the error 
    stems from the incorrectly filled email field.

    test_message_required():
    This test verifies that a populated contact form which is missing a 
    message input is not submitted, and that the error stems from the missing
    message field input.

    test_message_max_length_200_char():
    This test verifies that a completed populated contact form is not submitted
    unless the message input is less than 200 characters, and that the error 
    stems from the overfilled message field.

    Note: The application form on the user side does not allow the insertion 
    of more than 200 characters.

    test_form_is_valid():
    This test verifies that a correctly filled out contact form is successfully submitted.
    (add django success message testing to this.)
    '''

    def test_name_required(self):
        contact_form = ContactForm({
            'name': '',
            'email': 'john.test@gmail.com',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('name', contact_form.errors.keys())
        self.assertEqual(contact_form.errors['name'][0], 'This field is required.')

    
    def test_email_required(self):
        contact_form = ContactForm({
            'name': 'John',
            'email': '',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('email', contact_form.errors.keys())
        self.assertEqual(contact_form.errors['email'][0], 'This field is required.')


    def test_email_correct_format(self):
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('email', contact_form.errors.keys())
        self.assertEqual(contact_form.errors['email'][0], 'Enter a valid email address.')

    
    def test_message_required(self):
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.test@gmail.com',
            'message': ''
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('message', contact_form.errors.keys())
        self.assertEqual(contact_form.errors['message'][0], 'This field is required.')

    
    def test_message_max_length_200_chars(self):
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.test@gmail.com',
            'message': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed posuere, 
            sem at consequat convallis, elit magna egestas elit, vel ullamcorper nunc 
            magna vehicula risus. Pellentesque id leo sed odio tristique fermentum sit amet id sem. 
            Nullam vulputate varius elit. Suspendisse maximus ex ut enim vulputate, id 
            efficitur arcu pharetra. Orci varius natoque penatibus et magnis dis parturient 
            montes, nascetur ridiculus mus. Ut est arcu, tincidunt non turpis vel, volutpat 
            fermentum purus.
            '''
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('message', contact_form.errors.keys())


    def test_form_is_valid(self):
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.smith@gmail.com',
            'message': 'just testing your form!'
            })
        self.assertTrue(contact_form.is_valid())

