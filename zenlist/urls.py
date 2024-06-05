"""
URL configuration for zenlist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('reviews/delete-review/<int:id>', delete_review, name='delete-review'),
    path('workspaces/', include('workspace.urls'), name='space-urls'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
