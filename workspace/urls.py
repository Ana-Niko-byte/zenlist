from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkspaceListView.as_view(), name='spaces'),
    path('<slug:slug>/', views.workspace_detail, name='full_workspace'),
    # set up url for task editing form.
    # path('<slug:slug>/task_edit/<int:task_id>', views.edit_task, name='task_edit'),
]