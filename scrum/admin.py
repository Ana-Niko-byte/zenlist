from django.contrib import admin
from .models import Scrum, Feature
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Scrum)
class ScrumAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Feature)
class FeatureAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)