from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.WorkspaceListView.as_view(), name='spaces'),
]