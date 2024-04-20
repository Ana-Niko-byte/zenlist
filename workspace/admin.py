from django.contrib import admin
from .models import Workspace
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Workspace)
class WorkspaceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'creator', 'created_on')
    search_fields = ['title', 'creator']