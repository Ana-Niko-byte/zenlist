from django.test import TestCase
from django.urls import resolve, reverse
from zenlist.urls import *


class TestScrumURLs(TestCase):
    '''
    A class for testing URLs associated with Scrum Views.

    Methods:
    def test_hello_resolves():
        Reverses the URL name and checks if it returns the correct
        FBV of HelloScrum.
        Asserts HelloScrum is resolved from 'hello'.

    def test_contact_resolves():
        Reverses the URL name and checks if it returns the correct
        FBV of Contact_Me.
        Asserts Contact_Me is resolved from 'contact'.

    def test_reviews_resolves():
        Reverses the URL name and checks if it returns the correct
        FBV of Zenlist_Reviews.
        Asserts Zenlist_Reviews is resolved from 'reviews'.
    '''
    def test_hello_resolves(self):
        '''
        Asserts FBV HelloScrum is resolved from 'hello'.
        '''
        path = reverse('hello')
        self.assertEqual(resolve(path).func, HelloScrum)

    def test_contact_resolves(self):
        '''
        Asserts FBV Contact_Me is resolved from 'contact'.
        '''
        path = reverse('contact')
        self.assertEqual(resolve(path).func, Contact_Me)

    def test_reviews_resolves(self):
        '''
        Asserts FBV Zenlist_Reviews is resolved from 'reviews'.
        '''
        path = reverse('reviews')
        self.assertEqual(resolve(path).func, Zenlist_Reviews)
        