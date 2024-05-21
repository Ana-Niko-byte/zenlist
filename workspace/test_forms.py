from django.test import TestCase
from .forms import WorkspaceForm

class WorkspaceFormTest(TestCase):

    def test_form_is_valid(self):
        ws_form = WorkspaceForm({'title': 'Testing Workspace Addition'})
        self.assertTrue(ws_form.is_valid())