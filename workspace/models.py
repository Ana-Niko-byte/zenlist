from django.db import models
from django.contrib.auth.models import User
import datetime

STATUSES = (
    ('TO-DO', 'To Do'),
    ('IN-PROGRESS', 'In Progress'),
    ('DONE', 'Completed'),
)

PRIORITIES = (
    ('CRITICAL', 'Critical'),
    ('MAJOR', 'Major'),
    ('MINOR', 'Minor'),
    ('NICE-TO-HAVE', 'Nice to have!'),
)

class Workspace(models.Model):
    """
    Represents a Workspace model with basic 'environment' information. Within admin, sorted by last-created.

    Attributes: 
    title = The name of the workspace.
    creator = A registered user who has created a workspace.
    created_on = The time and date the workspace was created on.
    updated_on = The time and date the workspace was updated on. 

    Returns: (str) the title of the workspace as a string. 
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created_on"]

    def __str__(self):
        return f"Title of Workspace: {self.title}"


class Task(models.Model):
    """
    Represents a TASK model with detailed information. Within admin, sorted by last-created.

    Attributes: 
    name = The name of the task given by the user.
    notes = A textfield for users to add notes. These notes can be edited and/or deleted.
    creator = A registered user who has created the task.
    workspace = A registered user's workspace to which the task is associated. 
    status = A charfield field for sorting the task.
    priority = A charfield field for sorting the task by its priority.
    due_date = The date the task is due on. Default set to the date the task was created.
    date_created = The date and time the task was created on.
    last_modified = The date and time the task was last modified.
    updated = A boolean field for determining whether a task has been updated after it was created.

    Returns: (str) the title of the task as a string. 
    """
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, default='')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_creator')
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='workspace_tasks')
    status = models.CharField(choices=STATUSES, null=False, default='MINOR')
    priority = models.CharField(choices=PRIORITIES, default='TO-DO')
    due_date = models.DateField(default=datetime.date.today)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    last_modified = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ["due_date"]
    
    def __str__(self):
        return f"task '{self.name}'"
    
