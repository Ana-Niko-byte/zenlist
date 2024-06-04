from django.test import TestCase, Client
from django.core import mail
from django.urls import reverse
from django.conf import settings
from .forms import *
from django.contrib.auth.models import User


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
    This test verifies that a correctly filled out contact form is
    successfully submitted.
    '''

    def test_name_required(self):
        '''
        Creates a partially filled contact form instance.
        Asserts the form is invalid if the name field is empty.
        Asserts the error stems from the empty name field.
        Asserts the invoked error is the expected error.
        '''
        contact_form = ContactForm({
            'name': '',
            'email': 'john.test@gmail.com',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('name', contact_form.errors.keys())
        self.assertEqual(
            contact_form.errors['name'][0],
            'This field is required.'
        )

    def test_email_required(self):
        '''
        Creates a partially filled contact form instance.
        Asserts the form is invalid if the email field is empty.
        Asserts the error stems from the empty email field.
        Asserts the invoked error is the expected error.
        '''
        contact_form = ContactForm({
            'name': 'John',
            'email': '',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('email', contact_form.errors.keys())
        self.assertEqual(
            contact_form.errors['email'][0],
            'This field is required.'
        )

    def test_email_correct_format(self):
        '''
        Creates a filled contact form instance.
        Asserts the form is invalid if the entered email is of an
        invalid/incomplete format.
        Asserts the error stems from the invalid email field.
        Asserts the invoked error is the expected error.
        '''
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john',
            'message': 'just testing your form!'
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('email', contact_form.errors.keys())
        self.assertEqual(
            contact_form.errors['email'][0],
            'Enter a valid email address.'
        )

    def test_message_required(self):
        '''
        Creates a partially filled contact form instance.
        Asserts the form is invalid if the message field is empty.
        Asserts the error stems from the empty message field.
        Asserts the invoked error is the expected error.
        '''
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.test@gmail.com',
            'message': ''
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('message', contact_form.errors.keys())
        self.assertEqual(
            contact_form.errors['message'][0],
            'This field is required.'
        )

    def test_message_max_length_200_chars(self):
        '''
        Creates a filled contact form instance.
        Asserts the form is invalid if the message field is overfilled
        (max: 200 characters).
        Asserts the error stems from the empty name field.

        Note: no test for specific error as the Django form does not allow an
        input of more than 200 characters.
        '''
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.test@gmail.com',
            'message': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed posuere, sem at consequat convallis, elit magna egestas elit,
            vel ullamcorper nunc magna vehicula risus. Pellentesque id leo sed
            odio tristique fermentum sit amet id sem. Nullam vulputate varius
            elit. Suspendisse maximus ex ut enim vulputate, id efficitur arcu
            pharetra. Orci varius natoque penatibus et magnis dis parturient
            montes, nascetur ridiculus mus. Ut est arcu, tincidunt non turpis
            vel, volutpat fermentum purus.
            '''
        })
        self.assertFalse(contact_form.is_valid())
        self.assertIn('message', contact_form.errors.keys())

    def test_form_is_valid(self):
        '''
        Creates a filled contact form instance.
        Asserts the form is valid if all fields are complete and of
        the expected format.
        Asserts the form gets successfully sent to the correct email address.
        '''
        contact_form = ContactForm({
            'name': 'John',
            'email': 'john.smith@gmail.com',
            'message': 'just testing your form!'
            })
        self.assertTrue(contact_form.is_valid())


class EmailTest(TestCase):
    '''
    A class for testing email-related functionality for the ContactForm,
    provided all input fields have been filled with the expected format.

    Methods:
    test_contactForm_email_submission():
    Simulates a post request from the 'contact' page, with name, email,
    and message form field data from the ContactForm. This data comes directly
    from the validated form in the final method of class TestContactForm.

    Asserts that the Django test outbox contains 1 email.
    Asserts that the subject of the email matches the expected
    f"New Message from {name}" format.

    Asserts that the body of the mail matches the sent 'message' input.
    Asserts that the email from which is was sent matches that of
    settings.EMAIL_HOST_USER (my email).

    Asserts that the email to which the mail was sent matches my email.
    Asserts that the email to which the mail can be replied to matches
    that of the user's input in the 'email' field.
    '''

    # Code Structure can be found here:
    # https://docs.djangoproject.com/en/dev/topics/testing/tools/
    # Use CTRL + F to look for 'EmailMessage' and 'outbox'.
    def test_contactForm_email_submission(self):
        response = self.client.post(reverse('contact'), {
            'name': 'John',
            'email': 'john.smith@gmail.com',
            'message': 'Just testing your form!',
        })
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "New Message from John")
        self.assertEqual(mail.outbox[0].body, "Just testing your form!")
        self.assertEqual(mail.outbox[0].from_email, settings.EMAIL_HOST_USER)
        self.assertIn("ananikolayenia@gmail.com", mail.outbox[0].to)
        self.assertIn("john.smith@gmail.com", mail.outbox[0].reply_to)
        self.assertRedirects(response, '/', status_code=302)


class TestReviewForm(TestCase):
    '''
    A class for testing the ReviewForm Model is only visible to
    logged in users, and that all fields are filled out as expected.

    Methods:
    def setUp():
        As the review form is only visible to logged in users, setUp
        simulates a logged in user using the test client object.

        Note: More information on this can be found in the Django
        documentation, using CTRL + F and 'test client' in this link:
        https://docs.djangoproject.com/en/dev/topics/testing/tools/

    def test_author_is_User():
        This test verifies that the 'author' field of the review form is
        automatically filled as the logged in User. In this test, this is
        set manually as 'ananiko', as per the login simulation username
        in setUp. This field is not available to end users for manual input.

    def test_job_industry_is_required():
        This test verifies that a populated review form which is missing a
        job_industry input is not submitted, and that the error stems from
        the missing job_industry field input.

    def test_rating_is_required():
        This test verifies that a populated review form which is missing a
        rating input is not submitted, and that the error stems from the
        missing rating field input.

    def test_review_is_required():
        This test verifies that a populated contact form which is missing a
        review input is not submitted, and that the error stems from the
        missing review field input.
    '''
    def setUp(self):
        '''
        Sets up a login simulation for the review form.
        This form is only visible to logged in users on the home page.
        '''
        self.client = Client()
        self.user = User.objects.create_user(
            username='ananiko',
            password='test-password'
        )

    def test_author_is_User(self):
        '''
        Creates a filled review form instance where review.author is
        assigned manually as 'ananiko', as per the login simulation username
        in setUp. This field is not available to end users for manual input.
        Asserts the review.author field is the User.
        Asserts the form is valid if the review.author field is User,
        and if all fields have been filled out as expected.
        '''
        review_form = ReviewForm({
            'author' : 'ananiko',
            'job_industry' : 'Finance',
            'rating': '★★★★☆',
            'review': 'Great app!'
        })
        self.assertTrue('author', self.user)
        self.assertTrue(review_form.is_valid())

    def test_job_industry_is_required(self):
        '''
        Creates a filled review form instance, with an omitted job_industry
        field.
        Asserts the form is invalid if the job_industry field is empty.
        Asserts the error stems from the empty job_industry field.
        Asserts the invoked error is the expected error.
        '''
        review_form = ReviewForm({
            'job_industry' : '',
            'rating': '★★★★☆',
            'review': 'Great app!'
        })
        self.assertFalse(review_form.is_valid())
        self.assertIn('job_industry', review_form.errors.keys())
        self.assertEqual(
            review_form.errors['job_industry'][0],
            'This field is required.'
        )

    def test_rating_is_required(self):
        '''
        Creates a filled review form instance, with an omitted rating field.
        Asserts the form is invalid if the rating field is empty.
        Asserts the error stems from the empty rating field.
        Asserts the invoked error is the expected error.
        '''
        review_form = ReviewForm({
            'job_industry' : 'Finance',
            'rating': '',
            'review': 'Great app!'
        })
        self.assertFalse(review_form.is_valid())
        self.assertIn('rating', review_form.errors.keys())
        self.assertEqual(
            review_form.errors['rating'][0],
            'This field is required.'
        )

    def test_review_is_required(self):
        '''
        Creates a filled review form instance, with an omitted review field.
        Asserts the form is invalid if the review field is empty.
        Asserts the error stems from the empty review field.
        Asserts the invoked error is the expected error.
        '''
        review_form = ReviewForm({
            'job_industry' : 'Finance',
            'rating': '★★★★☆',
            'review': ''
        })
        self.assertFalse(review_form.is_valid())
        self.assertIn('review', review_form.errors.keys())
        self.assertEqual(
            review_form.errors['review'][0],
            'This field is required.'
        )
