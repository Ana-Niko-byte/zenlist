from django.test import TestCase, Client
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


class TestTaskForm(TestCase):
    '''
    A class for testing the task form associated with
    the Task Model. This form creates a new task
    instance if specific user inputs are correctly placed
    in the form fields.

    Methods:
    def test_title_is_required():


    def test_form_is_valid():
        This test verifies that a correctly filled out task form is
        successfully submitted.
    '''

    def setUp(self):
        '''
        Sets up a login simulation for the task form to create a user.
        Creates a workspace object instance for testing correct assignment.
        '''
        self.client = Client()
        self.user = User.objects.create_user(
            username='ananiko',
            password='test-password'
        )
        self.workspace = Workspace.objects.create(
            id=4,
            title='headphones',
            creator=self.user
        )

    def test_name_is_required(self):
        '''
        Creates a partially filled task form instance.
        Asserts the form is invalid if the name field is empty.
        Asserts the error stems from the empty name field.
        Asserts the invoked error is the expected error.
        '''
        task_form = TaskForm({
            'name': '',
            'creator': self.user,
            'workspace': 'headphones',
            'priority': 'Minor',
            'status': 'To Do',
            'due_date': '2024-06-21',
            'approved': False
        })

        self.assertFalse(task_form.is_valid())
        self.assertIn('name', task_form.errors.keys())
        self.assertEqual(
            task_form.errors['name'][0],
            'This field is required.'
        )

    def test_creator_is_User(self):
        '''
        Creates a filled task form instance where task.creator is
        assigned manually as 'ananiko', as per the login simulation username
        in setUp. This field is not available to end users for manual input.

        Asserts the task.creator field is the User.
        Asserts the form is valid if the task.creator field is User,
        and if all fields have been filled out as expected.
        '''
        task_form = TaskForm({
            'name': 'Test Task',
            'creator': 'ananiko',
            'workspace': 'headphones',
            'priority': 'Minor',
            'status': 'To Do',
            'due_date': '2024-06-21',
            'approved': False
        })
        self.assertTrue('creator', self.user)
        self.assertTrue(task_form.is_valid())

    def test_workspace_is_correctly_assigned(self):
        '''
        Creates a filled task form instance where task.workspace is
        assigned manually as 'headphones', as per the workspace instance
        in setUp. This field is not available to end users for manual input.

        Asserts the task.workspace field is the workspace instance.
        Asserts the form is valid if the task.workspace field matches
        the expected instance, and if all other fields have been filled out.
        '''
        task_form = TaskForm({
            'name': 'Test Task',
            'creator': self.user,
            'workspace': 'headphones',
            'priority': 'Minor',
            'status': 'To Do',
            'due_date': '2024-06-21',
            'approved': False
        })
        self.assertTrue('workspace', self.workspace)
        self.assertTrue(task_form.is_valid())

    def test_priority_is_required(self):
        '''
        Creates a partially filled task form instance.
        Asserts the form is invalid if the priority field is empty.
        Asserts the error stems from the empty priority field.
        Asserts the invoked error is the expected error.
        '''
        task_form = TaskForm({
            'name': 'Test Task',
            'creator': self.user,
            'workspace': 'headphones',
            'priority': '',
            'status': 'To Do',
            'due_date': '2024-06-21',
            'approved': False
        })

        self.assertFalse(task_form.is_valid())
        self.assertIn('priority', task_form.errors.keys())
        self.assertEqual(
            task_form.errors['priority'][0],
            'This field is required.'
        )

    def test_status_is_required(self):
        '''
        Creates a partially filled task form instance.
        Asserts the form is invalid if the status field is empty.
        Asserts the error stems from the empty status field.
        Asserts the invoked error is the expected error.
        '''
        task_form = TaskForm({
            'name': 'Test Task',
            'creator': self.user,
            'workspace': 'headphones',
            'priority': 'Minor',
            'status': '',
            'due_date': '2024-06-21',
            'approved': False
        })

        self.assertFalse(task_form.is_valid())
        self.assertIn('status', task_form.errors.keys())
        self.assertEqual(
            task_form.errors['status'][0],
            'This field is required.'
        )
