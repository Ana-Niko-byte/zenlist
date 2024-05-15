from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Count
from .models import Workspace, Task
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
    context_object_name = 'spaces'

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
        """
        Handles the creation of a workspace via the provided form.
        """
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

class WorkspaceDeleteView(DeleteView):
    """
    Deletes a workspace. 
    """
    model = Workspace
    # !!! Check routing for this template as it does not seem to appear. !!!
    template_name = 'workspace/ws_confirm_delete.html'
    success_url = 'spaces'

@login_required
def update_ws_task(request, id):
    """
    A view for updating the contents of an existing task. 
    This will be changed to a pop up modal to avoid the need for additional routing.
    """
    task_for_update = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        edit_task_form = TaskForm(data=request.POST, instance=task_for_update)
        if edit_task_form.is_valid():
            edit_task_form.save()
            return redirect('full_workspace', slug=task_for_update.workspace.slug)
    else:
        edit_task_form = TaskForm(instance=task_for_update)

    context = {
        'task_for_update': task_for_update,
        'edit_task_form': edit_task_form,
    }
    return render(request, 'workspace/update.html', context)

def delete_ws_task(request, id):
    """
    A modal to delete a task.
    """
    task_for_deletion = get_object_or_404(Task, id=id)
    if task_for_deletion.creator == request.user:
        task_for_deletion.delete()
        return redirect ('full_workspace', slug=task_for_deletion.workspace.slug)

# def comment_delete(request, slug, comment_id):
#     """
#     view to delete comment
#     """
#     queryset = Post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     comment = get_object_or_404(Comment, pk=comment_id)

#     if comment.author == request.user:
#         comment.delete()
#         messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
#     else:
#         messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

#     return HttpResponseRedirect(reverse('post_detail', args=[slug]))