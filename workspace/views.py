from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Workspace

class WorkspaceListView(generic.ListView):
    model = Workspace
    template_name = 'workspace/workspace_list.html'
    context_object_name = 'spaces'

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
    pass
    # queryset = Workspace.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
    # comments = post.comments.all().order_by("-created_on")
    # comment_count = post.comments.filter(approved=True).count()
    # if request.method == "POST":
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         messages.add_message(
    #     request, messages.SUCCESS,
    #     'Comment submitted and awaiting approval'
    # )
    # comment_form = CommentForm()
    # return render(
    #     request,
    #     "blog/post_detail.html",
    #     {
    #         "post": post,
    #         "comments": comments,
    #         "comment_count": comment_count,
    #         "comment_form": comment_form,
    #     },
    # )