from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from workspace.models import *
from django.utils.text import slugify


class TestWorkspaceViews(TestCase):
    '''
    A class to test views and status codes associated with the Workspace app.

    Methods:
    def setUp():
        Creates a Client Instance.
        Creates a User instance.
        Simulates user log in to allow for URL testing that require user
        authentication and the creation of workspaces and tasks.
        Simulates the creation of a workspace.
        Simulates the creation of a task.
        Sets up URLs for testing for views associated with the Workspace app.

    def test_workspaces_page_GET():
        This test asserts that the common workspaces URL is retrieved and
        rendered successfully and as expected.

    def test_workspace_detail_page_GET():
        This test asserts that the workspace detail URL is retrieved and
        rendered successfully with the expected workspace slug as an argument.

    def test_delete_workspace_view():
        This test asserts that the workspace delete URL is retrieved and and
        rendered successfully with the expected workspace id as an argument.

    def test_task_update_view_POST():
        This test asserts that the task update URL is retrieved and and
        rendered successfully with the expected workspace slug and task id
        as arguments.

    def test_task_delete_url():
        This test asserts that the task delete URL is retrieved and and
        rendered successfully with the expected workspace slug and task id
        as arguments.
    '''

    def setUp(self):
        '''
        Creates a Client Instance.
        Creates a User instance.
        Simulates user log in to allow for URL testing that require user
        authentication and the creation of workspaces and tasks.
        Simulates the creation of a workspace.
        Simulates the creation of a task.
        Sets up URLs for testing for views associated with the Workspace app.

        URLS:
        Common Workspace URL
        Workspace Detail URL
        Delete Workspace URL
        Update Task URL
        Delete Task URL
        '''
        self.Client = Client()

        self.user = User.objects.create_user(
            username='ananiko',
            password='test-password'
        )
        self.client.login(
            username='ananiko',
            password='test-password'
        )

        title = 'Test Workspace'
        self.workspace = Workspace.objects.create(
            id=4,
            title=title,
            slug=slugify(title),
            creator=self.user
        )

        self.task = Task.objects.create(
            id=6,
            name='Test Task',
            notes='Testing Task Model',
            creator=self.user,
            workspace=self.workspace,
            priority='Minor',
            status='To Do',
            due_date='2024-07-21'
        )

        self.workspaces_url = reverse('spaces')
        self.user_workspace_url = reverse(
            'full_workspace',
            args=[self.workspace.slug]
            )
        self.workspace_delete_url = reverse(
            'delete_workspace',
            args=[self.workspace.id]
            )
        self.task_update_url = reverse(
            'task_edit',
            args=[self.workspace.slug, self.task.id]
            )
        self.task_delete_url = reverse(
            'task_delete',
            args=[self.workspace.slug, self.task.id]
            )

    def test_workspaces_page_GET(self):
        '''
        Retrieves the common workspaces page URL and asserts if the view
        renders successfully.
        Asserts the user is registered and signed in.
        Asserts status code is 200.
        Asserts the template used matches the expected from views.py.
        '''
        response = self.client.get(self.workspaces_url)
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workspace/ws_list.html')

    def test_workspace_detail_page_GET(self):
        '''
        Retrieves the workspace instance detail URL and asserts if the view
        renders successfully.
        Asserts the user is registered and signed in.
        Asserts status code is 200.
        Assers the response contains the name of the workspace.
        Asserts the response contains the breadcrumb nav with class breadcrumb.
        Asserts the workspace id matches that of the instance id.
        Asserts the template used matches the expected from views.py.
        '''
        response = self.client.get(self.user_workspace_url)
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(response.status_code, 200)
        self.assertContains(response, self.workspace.title)
        self.assertContains(response, 'breadcrumb')
        self.assertEqual(response.context['workspace'].id, self.workspace.id)
        self.assertTemplateUsed(response, 'workspace/ws_detail.html')

    def test_delete_workspace_view(self):
        '''
        Retrieves the workspace delete URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        '''
        response = self.client.get(self.workspace_delete_url)
        self.assertTrue(response.status_code, 200)

    def test_task_update_view_POST(self):
        '''
        Retrieves the task update URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        '''
        response = self.client.get(self.task_update_url)
        self.assertTrue(response.status_code, 200)

    def test_task_delete_url(self):
        '''
        Retrieves the task delete URL and asserts if the view renders
        successfully.
        Asserts status code is 200.
        '''
        response = self.client.get(self.task_delete_url)
        self.assertTrue(response.status_code, 200)
