from django.contrib import admin
from .models import Scrum, Feature, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Scrum)
class ScrumAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Feature)
class FeatureAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('review',)