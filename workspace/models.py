from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created_on"]

    def __str__(self):
        return f"Title of Workspace: {self.title}"