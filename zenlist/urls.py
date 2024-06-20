from django.contrib import admin
from django.urls import path, include
from scrum.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', HelloScrum, name='hello'),
    path('contact/', Contact_Me, name='contact'),
    path('reviews/', Zenlist_Reviews, name='reviews'),
    path(
        'reviews/delete-review/<int:id>',
        delete_review,
        name='delete-review'
    ),
    path('workspaces/', include('workspace.urls'), name='space-urls'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
