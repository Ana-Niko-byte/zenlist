from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUSES = (
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)

PRIORITIES = (
    ('Critical', 'Critical'),
    ('Major', 'Major'),
    ('Minor', 'Minor'),
    ('Nice to have!', 'Nice to have!'),
)


class Workspace(models.Model):
    """
    Represents a Workspace model with basic 'environment' information.
    Within admin, sorted by last-created.

    Attributes:
    title = The name of the workspace.
    creator = A registered user who has created a workspace.
    created_on = The time and date the workspace was created on.
    updated_on = The time and date the workspace was updated on.

    Returns: (str) the title of the workspace as a string.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='creator'
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Title of Workspace: {self.title}"


class Task(models.Model):
    """
    Represents a TASK model with detailed information.
    Within admin, sorted by last-created.

    Attributes:
    name = The name of the task given by the user.
    notes = A textfield for users to add notes.
    These notes can be edited and/or deleted.
    creator = A registered user who has created the task.
    workspace = A registered user's workspace to which the task is associated.
    status = A charfield field for sorting the task.
    priority = A charfield field for sorting the task by its priority.
    due_date = The date the task is due on.
    Default set to the date the task was created.
    date_created = The date and time the task was created on.
    last_modified = The date and time the task was last modified.

    Returns: (str) the title of the task as a string.
    """
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, default='', max_length=100)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='task_creator'
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name='workspace_tasks'
    )
    priority = models.CharField(
        choices=PRIORITIES,
        max_length=15,
        default='Minor'
    )
    status = models.CharField(
        choices=STATUSES,
        max_length=15,
        default='To Do'
    )
    due_date = models.DateField(default=timezone.now)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return f"task '{self.name}'"
