from django.contrib import admin
from .models import Scrum
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Scrum)
class ScrumAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)