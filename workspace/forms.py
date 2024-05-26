from django import forms
from .models import Workspace, Task


class WorkspaceForm(forms.ModelForm):
    """
    A form for handling Workspace creation for registered users.
    """
    class Meta:
        model = Workspace
        fields = ('title',)
        labels = {
            'title' : 'Workspace Title: '
        }
    


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    """
    A form for handling Task additions to a workspace.
    """
    class Meta:
        model = Task
        fields = ('name', 'notes', 'status', 'priority', 'due_date',)
        # See README for widget code.
        widgets = {
            'due_date': DateInput(attrs={'type':'date'})
            },

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["due_date"].input_formats = ['%Y-%m-%d']
