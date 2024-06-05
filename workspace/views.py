from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils.text import slugify
# For Timezone Support
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.db.models import Count
from .models import Workspace, Task
from .forms import WorkspaceForm, TaskForm


@login_required
def workspace_detail(request, slug):
    """
    Display an individual instance of a workspace with tasks.
    """
    # retrieves the relevant workspace.
    workspace = get_object_or_404(Workspace, slug=slug)
    # retrieves all tasks associated with this workspace.
    all_tasks = workspace.workspace_tasks.all()
    all_task_count = all_tasks.count()

    todo = workspace.workspace_tasks.filter(status='To Do')
    progress = workspace.workspace_tasks.filter(status='In Progress')
    completed = workspace.workspace_tasks.filter(status='Completed')

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
        "workspace/ws_detail.html",
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
    """
    Display all user workspaces as a list. Queryset is filtered by creator.
    """
    model = Workspace
    template_name = 'workspace/ws_list.html'

    def get_queryset(self):
        user_workspaces = Workspace.objects.filter(creator=self.request.user)
        return user_workspaces

    def get_context_data(self, **kwargs):
        # For this code source, see README.
        data = super().get_context_data(**kwargs)
        data['user_workspaces'] = Workspace.objects.filter(
                creator=self.request.user
            )
        data['workspace_form'] = WorkspaceForm()

        # For information on annotate(), see README.
        ws_tasks = self.get_queryset().annotate(
            ws_task_count=Count('workspace_tasks')
        )
        data['ws_tasks'] = ws_tasks.order_by('-created_on')

        # Tasks that are due today
        # filter=Q because of complex querying
        due_tasks = self.get_queryset().annotate(
            due_count=Count(
                'workspace_tasks',
                filter=Q(
                    workspace_tasks__due_date=timezone.now().date()
                )
            )
        )
           
        data['due_tasks'] = due_tasks.order_by('-created_on')
        return data

    def post(self, request):
        """
        Handles the creation of a workspace via the provided form.
        """
        if request.method == "POST":
            workspace_form = WorkspaceForm(data=request.POST)
            if workspace_form.is_valid():
                workspace = workspace_form.save(commit=False)
                workspace.creator = request.user
                workspace.slug = slugify(workspace.title)
                workspace.updated_on = timezone.now().date()
                workspace.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Workspace created successfully!'
                )
                return redirect('spaces')
            # implement error handling here later.
        workspace_form = WorkspaceForm()


@login_required
def delete_ws(request, id):
    """
    FBV for deleting a workspace based on id retrieval.
    """
    workspace = get_object_or_404(Workspace, id=id)
    if workspace.creator == request.user:
        workspace.delete()
        return HttpResponseRedirect(reverse('spaces'))


def update_ws_task(request, slug, task_id):
    """
    A view for updating the contents of an existing task.
    """
    if request.method == 'POST':
        queryset = Workspace.objects.filter(creator=request.user)
        workspace = get_object_or_404(queryset, slug=slug)
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(data=request.POST, instance=task)

        if form.is_valid():
            task = form.save(commit=False)
            task.workspace = workspace
            # To save the date of a task modification as a workspace change.
            workspace.updated_on = timezone.now().date()
            workspace.save()
            task.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your task has been updated successfully!"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                '''Oh no! An error occurred while trying to update 
                your task, please try again later.'''
            )
    return HttpResponseRedirect(reverse('full_workspace', args=[slug]))


@login_required
def delete_ws_task(request, slug, id):
    """
    A modal to delete a task.
    """
    task_for_deletion = get_object_or_404(Task, id=id)
    if task_for_deletion.creator == request.user:
        task_for_deletion.delete()
    # Note to future self because this bug took f* ages, keys must be in ''!
    return HttpResponseRedirect(reverse(
        'full_workspace',
        kwargs={'slug':task_for_deletion.workspace.slug}))
