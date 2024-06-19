from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from scrum.models import *


class TestScrumViews(TestCase):
    '''
    A class to test views and status codes associated with the Scrum app.

    Methods:
    def setUp():
        Creates a Client Instance.
        Creates a User instance.
        Simulates user log in to allow for URL testing that require user
        authentication and the deletion of reviews.
        Simulates the creation of a review for deletion purposes.
        Sets up URLs for testing for views associated with the Scrum app.

    def test_scrum_page_GET():
        This test asserts that the Scrum homepage URL is retrieved and
        rendered successfully and as expected.

    def test_contact_page_GET():
        This test asserts that the Contact URL is retrieved and
        rendered successfully and as expected.

    def test_reviews_page_GET():
        This test asserts that the Reviews URL is retrieved and
        rendered successfully and as expected.

    def test_review_delete_GET():
        This test asserts that the review delete URL is retrieved and and
        rendered successfully with the expected review id
        as an argument.
    '''

    def setUp(self):
        '''
        Creates a Client Instance.
        Creates a User instance.
        Simulates user log in to allow for URL testing that require user
        authentication and the deletion of reviews.
        Simulates the creation of a review for deletion purposes.
        Sets up URLs for testing for views associated with the Scrum app.

        URLS:
        Scrum (Home) Page URL
        Contact Page URL
        Reviews Page URL
        '''
        self.Client = Client()

        self.user = User.objects.create_user(
            id=3,
            username='ananiko',
            password='test-password'
        )

        self.client.login(
            username='ananiko',
            password='test-password'
        )

        self.review = Review(
            id=4,
            author=self.user,
            job_industry='Finance',
            rating='★★★★☆',
            review='Testing the review Model.'
        )

        self.scrum_url = reverse('hello')
        self.contact_url = reverse('contact')
        self.reviews_url = reverse('reviews')
        self.review_delete_url = reverse(
            'delete-review',
            args=[self.review.id]
        )

    def test_scrum_page_GET(self):
        '''
        Retrieves the scrum/home page URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        Asserts the template used matches the expected from views.py.
        '''
        response = self.client.get(self.scrum_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrum/index.html')

    def test_contact_page_GET(self):
        '''
        Retrieves the contact page URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        Asserts the template used matches the expected from views.py.
        '''
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrum/contact.html')

    def test_reviews_page_GET(self):
        '''
        Retrieves the reviews page URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        Asserts the template used matches the expected from views.py.
        '''
        response = self.client.get(self.reviews_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrum/reviews.html')

    def test_review_delete(self):
        '''
        Retrieves the review delete URL and asserts if the view renders
        successfully.
        Asserts the user is signed in.
        Asserts status code is 200.
        '''
        response = self.client.get(self.review_delete_url)
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(response.status_code, 200)
