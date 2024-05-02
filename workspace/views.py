from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Workspace

class WorkspaceListView(generic.ListView):
    model = Workspace
    template_name = 'workspace/workspace_list.html'
    context_object_name = 'spaces'

    def get_queryset(self):
        user_workspaces = Workspace.objects.filter(creator=self.request.user)
        return user_workspaces
    
    def get_context_data(self, **kwargs):
        # For this code source, please see README.
        data = super().get_context_data(**kwargs)
        data['user_workspaces'] = Workspace.objects.filter(creator=self.request.user)
        return data

def workspace_detail(request, slug):
    """
    Display an individual instance of a workspace with tasks.
    """
    queryset = Workspace.objects.all()
    workspace = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "workspace/workspace_detail.html",
        {
            'workspace': workspace
        },
    )