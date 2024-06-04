from django.test import TestCase, Client
from .models import *


class TestScrumModel(TestCase):
    '''
    A class to test the Scrum Model.

    Methods:
    def setUp():
        Simulates the logging in of a user for review model assertion,
        and creates instances for the Scrum and Review models.

    def test_scrum_model_creation():
        Runs a series of asserions for each Scrum Model field to validate
        the expected values of the instance.

    def test_review_model_creation():
        Runs a series of assertions for each Review Model field to validate
        the expected values of the instance.

    def test_user_deletion_cascade():
        Deletes the current logged in user and checks whether the
        user's reviews were deleted as well, as per cascade.
    '''
    def setUp(self):
        '''
        Simulates the logging in of a user for the review model.
        Creates a Scrum Model instance for database assertion testing.
        Creates a Review Model instance for database assertion testing.
        '''
        self.client = Client()
        self.user = User.objects.create_user(
            username='ananiko',
            password='test-password'
        )

        self.scrum = Scrum(
            id=1,
            title='Test title',
            content='Testing the scrum Model.'
        )

        self.review = Review(
            id=4,
            author=self.user,
            job_industry='Finance',
            rating='★★★★☆',
            review='Testing the review Model.'
        )

    def test_scrum_model_creation(self):
        '''
        Asserts whether the scrum id is 1, as per model setup.
        Asserts whether the scrum title is 'Test title', as per model setup.
        Asserts whether the scrum content is 'Testing the scrum Model.',
        as per model setup.
        '''
        self.assertEqual(self.scrum.id, 1)
        self.assertEqual(self.scrum.title, 'Test title')
        self.assertEqual(self.scrum.content, 'Testing the scrum Model.')

    def test_review_model_creation(self):
        '''
        Asserts whether the review id is 4, as per model setup.
        Asserts whether the review author is the logged in user,
        as per model setup.
        Asserts whether the review job_industry is 'Finance', as per model
        setup.
        Asserts whether the review rating is '★★★★☆', as per model setup.
        Asserts whether the 'review' field is 'Testing the review Model.',
        as per model setup.
        '''
        self.assertEqual(self.review.id, 4)
        self.assertEqual(self.review.author, self.user)
        self.assertEqual(self.review.job_industry, 'Finance')
        self.assertEqual(self.review.rating, '★★★★☆')
        self.assertEqual(self.review.review, 'Testing the review Model.')

    def test_user_deletion_cascade(self):
        '''
        Deletes the current user.
        Asserts if that user's reviews are also deleted.
        '''
        self.user.delete()
        self.assertEqual(len(Review.objects.all()), 0)
