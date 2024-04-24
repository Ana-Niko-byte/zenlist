from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.WorkspaceListView.as_view(), name='spaces'),
    path('<slug:slug>/', views.workspace_detail, name='full_workspace'),
]