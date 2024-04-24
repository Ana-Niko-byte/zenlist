from django.shortcuts import render
from django.views import generic
from .models import Workspace

class WorkspaceListView(generic.ListView):
    model = Workspace
    template_name = 'workspace/workspace_list.html'
    context_object_name = 'spaces'

# def WorkspaceList(request):
#     model = Workspace
#     space = Workspace.objects.all().first()
#     template_name = 'workspace/workspace_list.html'

#     context = {
#         'space' : space,
#         }
    
#     return render(
#         request,
#         "workspace/workspace_list.html",
#         context
#     )