from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.utils.text import slugify
from django.contrib import messages
from .models import Workspace
from .forms import WorkspaceForm, TaskForm

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
        data['workspace_form'] = WorkspaceForm()
        return data
    
    def post(self, request):
        if request.method == "POST":
            workspace_form = WorkspaceForm(data=request.POST)
            if workspace_form.is_valid():
                workspace = workspace_form.save(commit=False)
                workspace.creator = request.user
                workspace.slug = slugify(workspace.title)
                workspace.save()
                messages.add_message(
                request, messages.SUCCESS,
                'Workspace created successfully!'
                )
                return redirect('spaces')
            # implement error handling here later.
        workspace_form = WorkspaceForm()
    

def workspace_detail(request, slug):
    """
    Display an individual instance of a workspace with tasks.
    """
    queryset = Workspace.objects.all()
    workspace = get_object_or_404(queryset, slug=slug)
    tasks = workspace.workspace_tasks.all()
    to_do_tasks = workspace.workspace_tasks.filter(status='TO-DO')
    progress_tasks = workspace.workspace_tasks.filter(status='IN-PROGRESS')
    done_tasks = workspace.workspace_tasks.filter(status='DONE')
    to_do_task_count = to_do_tasks.count()
    progress_task_count = progress_tasks.count()
    done_task_count = done_tasks.count()
    task_form = TaskForm()

    return render(
        request,
        "workspace/workspace_detail.html",
        {
            'workspace': workspace,
            'tasks': tasks,
            'task_form': task_form,
            'to_do': to_do_tasks,
            'in_progress': progress_tasks,
            'completed': done_tasks,
            'to_do_task_count': to_do_task_count,
            'progress_task_count': progress_task_count,
            'done_task_count': done_task_count
        },
    )