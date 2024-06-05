from django.test import TestCase
from django.urls import reverse, resolve
from .views import *


class TestWorkspaceURLs(TestCase):
    '''
    A class for testing URLs associated with Workspace Views.

    Methods:
    def test_workspace_list_resolves():
        Reverses the URL name and checks if it returns the correct
        CBV of WorkspaceListView.
        Asserts WorkspaceListView is resolved from 'spaces'.

    def test_workspace_detail_resolves():
        Reverses the URL name with arguments [slug] and checks if it
        returns the correct FBV of workspace_detail.
        Asserts workspace_detail is resolved from 'full_workspace'.

    def test_workspace_delete_resolves():
        Reverses the URL name with arguments [int:id] and checks if it
        returns the correct FBV of delete_ws.
        Asserts delete_ws is resolved from 'delete_workspace'.

    def test_task_edit_resolves():
        Reverses the URL name with arguments [slug, int:id] and checks if it
        returns the correct FBV of update_ws_task.
        Asserts update_ws_task is resolved from 'task_edit'.

    def test_task_delete_resolves():
        Reverses the URL name with arguments [slug, int:id] and checks if it
        returns the correct FBV of delete_ws_task.
        Asserts delete_ws_task is resolved from 'task_delete'.
    '''
    def test_workspace_list_resolves(self):
        '''
        Asserts WorkspaceListView is resolved from 'spaces'.
        '''
        path = reverse('spaces')
        self.assertEqual(resolve(path).func.view_class, WorkspaceListView)

    def test_workspace_detail_resolves(self):
        '''
         Asserts workspace_detail is resolved from 'full_workspace'.
        '''
        path = reverse('full_workspace', args=['slug'])
        self.assertEqual(resolve(path).func, workspace_detail)

    def test_workspace_delete_resolves(self):
        '''
        Asserts delete_ws is resolved from 'delete_workspace'.
        '''
        path = reverse('delete_workspace', args=[4])
        self.assertEqual(resolve(path).func, delete_ws)

    def test_task_edit_resolves(self):
        '''
        Asserts update_ws_task is resolved from 'task_edit'.
        '''
        path = reverse('task_edit', args=['slug', 3])
        self.assertEqual(resolve(path).func, update_ws_task)

    def test_task_delete_resolves(self):
        '''
        Asserts delete_ws_task is resolved from 'task_delete'.
        '''
        path = reverse('task_delete', args=['slug', 6])
        self.assertEqual(resolve(path).func, delete_ws_task)
