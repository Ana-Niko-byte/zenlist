from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from .forms import *
from django.contrib.auth.models import User

class WorkspaceFormTest(TestCase):
    '''
    A class for testing the workspace form associated with
    the Workspace Model. This form creates a new workspace 
    instance if specific user inputs are correctly placed 
    in the form fields.

    Methods:
    def test_title_is_required():
        This test verifies that a populated workspace form which is missing a
        title input is not submitted, and that the error stems from the missing
        title field input.

    def test_form_is_valid():
        This test verifies that a correctly filled out workspace form is
        successfully submitted.

    '''
    def test_title_is_required(self):
        '''
        Creates a Workspace form instance with an empty
        title field.
        Asserts the form is invalid if the title field is empty.
        Asserts the error stems from the empty title field.
        Asserts the invoked error is the expected error.
        '''
        ws_form = WorkspaceForm({
            'title': ''
            })
        self.assertFalse(ws_form.is_valid())
        self.assertIn('title', ws_form.errors.keys())
        self.assertEqual(
            ws_form.errors['title'][0],
            'This field is required.'
        )

    def test_form_is_valid(self):
        '''
        Asserts a correctly filled form instance is valid.
        '''
        ws_form = WorkspaceForm({
            'title': 'Testing Workspace Addition'
            })
        self.assertTrue(ws_form.is_valid())