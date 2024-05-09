from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Count
from .models import Workspace
from .forms import WorkspaceForm, TaskForm

def workspace_detail(request, slug):
    """
    Display an individual instance of a workspace with tasks.
    """
    # retrieves the relevant workspace.
    workspace = get_object_or_404(Workspace, slug=slug)
    # retrieves all tasks associated with this workspace.
    all_tasks = workspace.workspace_tasks.all()
    all_task_count = all_tasks.count()

    todo = workspace.workspace_tasks.filter(status='TO-DO')
    progress = workspace.workspace_tasks.filter(status='IN-PROGRESS')
    completed = workspace.workspace_tasks.filter(status='DONE')

    if request.method == "POST":
            task_form = TaskForm(data=request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.creator = request.user
                task.workspace = workspace
                task.save()
                messages.add_message(
                request, messages.SUCCESS,
                'Task created successfully!'
                )
            # implement error handling here later.
    todo_count = todo.count()
    progress_count = progress.count()
    completed_count = completed.count()
    task_form = TaskForm()

    return render(
        request,
        "workspace/workspace_detail.html",
            {
            'workspace': workspace,
            'all_tasks': all_tasks,
            'total_count': all_task_count,
            'todo_tasks': todo,
            'progress_tasks': progress,
            'completed_tasks': completed,
            'todo_count': todo_count,
            'progress_count': progress_count,
            'completed_count': completed_count,
            'task_form': task_form,
        },
    )


class WorkspaceListView(generic.ListView):
    model = Workspace
    template_name = 'workspace/workspace_list.html'
    context_object_name = 'spaces'

    # analytic_list = zip(context_object_name, ws_tasks)

    def get_queryset(self):
        user_workspaces = Workspace.objects.filter(creator=self.request.user)
        return user_workspaces
    
    def get_context_data(self, **kwargs):
        # For this code source, see README.
        data = super().get_context_data(**kwargs)
        data['user_workspaces'] = Workspace.objects.filter(creator=self.request.user)
        data['workspace_form'] = WorkspaceForm()

        # For information on annotate(), see README.
        ws_tasks = self.get_queryset().annotate(ws_task_count=Count('workspace_tasks'))
        data['ws_tasks'] = ws_tasks
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