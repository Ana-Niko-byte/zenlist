from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Scrum(models.Model):
    """
    Represents a Scrum content model with Cloudinary fields for easy retrieval and document management.

    Attributes: 
    title = A reference to the paragraph title.
    image (CloudinaryField) = A field to store an image in Cloudinary. There is a default image for fallback purposes.
    updated_on = A reference to the date and time the extract was updated on.
    content = A reference to the main content.
    file (Cloudinary) = A field to store the Scrum Manual in PDF format in Cloudinary with help text.
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='default_image')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # models.FileField() was considered but Cloudinary was chosen for uniform asset management.
    file = CloudinaryField('document', default='scrum_manual', resource_type = 'auto', help_text='Download your Scrum manual here!')

    def __str__(self):
        return f'The title of this section is {self.title}'
    