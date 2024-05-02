from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    A form for handling Task additions to a workspace.
    """
    class Meta:
        model = Task
        fields = ('name', 'notes', 'status', 'priority', 'due_date',)