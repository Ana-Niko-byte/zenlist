from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Scrum(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='default_image')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f'The title of this section is {self.title}'