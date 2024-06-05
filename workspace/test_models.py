from django.test import TestCase, Client
from .models import *
from django.contrib.auth.models import User


class TestWorkspaceModel(TestCase):
    '''
    A class to test all models associated with the Workspace app.

    Methods:
    def setUp():
        Simulates user log in to allow the creation for workspaces and tasks.
        Simulates the creation of a workspace where workspace.creator field is
        automatically assigned the current User instance.
        Simulates the creation of a task where task.creator is automatically
        assigned the current User instance, and task.workspace is automatically
        assigned the current workspace.

    def test_workspace_model_creation():
        Runs a series of asserions for each Workspace Model field to validate
        the expected values of the instance.

    def test_task_model_creation():
        Runs a series of asserions for each Task Model field to validate
        the expected values of the instance.

    def test_workspace_delete_when_user_delete():
        Deletes the user and checks whether workspaces and tasks associated
        with the user were deleted as well, as per cascade.

    def test_task_delete_when_workspace_delete():
        Deletes the current workspace and checks whether tasks associated
        with the workspace were deleted as well, as per cascade.
    '''
    def setUp(self):
        '''
        Simulates user log in to allow the creation for workspaces and tasks.
        Simulates the creation of a workspace where workspace.creator field is
        automatically assigned the current User instance.
        Simulates the creation of a task where task.creator is automatically
        assigned the current User instance, and task.workspace is automatically
        assigned the current workspace.
        '''
        self.client = Client()
        self.user = User(
            id=3,
            username='ananiko',
            password='test-password'
        )

        self.workspace = Workspace(
            id=4,
            title='Test Workspace',
            creator=self.user
        )

        self.task = Task(
            id=6,
            name='Test Task',
            notes='Testing Task Model',
            creator=self.user,
            workspace=self.workspace,
            priority='Minor',
            status='To Do',
            due_date='2024-07-21',
            updated=False
        )

    def test_workspace_model_creation(self):
        '''
        Asserts the workspace id is 4, as per model setup.
        Asserts the workspace title is 'Test Workspace', as per model setup.
        Asserts the workspace creator's username is 'ananiko',
        as per user login.
        '''
        self.assertEqual(self.workspace.id, 4)
        self.assertEqual(self.workspace.title, 'Test Workspace')
        self.assertEqual(self.workspace.creator.username, 'ananiko')

    def test_task_model_creation(self):
        '''
        Asserts the task id is 6, as per model setup.
        Asserts the task name is 'Test Task', as per model setup.
        Asserts the task notes are 'Testing Task Model', as per model setup.
        Asserts the task creator's username is 'ananiko', as per user login.
        Asserts the task workspace title is 'Test Workspace',
        as per model setup.
        Asserts the task priority is 'Minor', as per model setup.
        Asserts the task status is 'To Do', as per model setup.
        Asserts the task due_date is '2024-07-21', as per model setup.
        Asserts whether the task updated field is set to False,
        as per model setup.
        '''
        self.assertEqual(self.task.id, 6)
        self.assertEqual(self.task.name, 'Test Task')
        self.assertEqual(self.task.notes, 'Testing Task Model')
        self.assertEqual(self.task.creator.username, 'ananiko')
        self.assertEqual(self.task.workspace.title, 'Test Workspace')
        self.assertEqual(self.task.priority, 'Minor')
        self.assertEqual(self.task.status, 'To Do')
        self.assertEqual(self.task.due_date, '2024-07-21')
        self.assertEqual(self.task.updated, False)

    def test_workspace_delete_when_user_delete(self):
        '''
        Deletes the current user.
        Asserts user's workspaces are also deleted.
        Asserts user's tasks are also deleted.
        '''
        self.user.delete()
        self.assertEqual(len(Workspace.objects.all()), 0)
        self.assertEqual(len(Task.objects.all()), 0)

    def test_task_delete_when_workspace_delete(self):
        '''
        Deletes the current workspace.
        Asserts tasks associated with that workspace are also deleted.
        '''
        self.workspace.delete()
        self.assertEqual(len(Task.objects.all()), 0)
