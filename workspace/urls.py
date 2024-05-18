from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkspaceListView.as_view(), name='spaces'),
    path('<slug:slug>/', views.workspace_detail, name='full_workspace'),
    path('delete/<int:id>/', views.delete_ws, name='delete_workspace'),
    path('<slug:slug>/update-task/<int:id>', views.update_ws_task, name='task_edit'),
    path('<slug:slug>/delete-task/<int:id>', views.delete_ws_task, name='task_delete'),
]