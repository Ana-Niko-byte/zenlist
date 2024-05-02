from django.contrib import admin
from .models import Workspace, Task
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Workspace)
class WorkspaceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'creator', 'created_on')
    search_fields = ['title', 'creator']

@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('name', 'workspace', 'priority', 'status', 'due_date')
    search_fields = ['name', 'status', 'priority']