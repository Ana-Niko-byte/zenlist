from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkspaceListView.as_view(), name='spaces'),
    path('<slug:slug>/', views.workspace_detail, name='full_workspace'),
    path('workspaces/delete/<int:pk>/', views.WorkspaceDeleteView.as_view(), name='delete_workspace'),
    path('update/task/<int:id>', views.update_ws_task, name='task_edit'),
]