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
    
class Feature(models.Model):
    """
    Represents a Feature element model with Cloudinary fields for easy retrieval and document management.

    Attributes: 
    title = A reference to the feature title.
    image (CloudinaryField) = A field to store the featured image in Cloudinary. There is a default image for fallback purposes.
    step = A reference to the feature number (max of 3).
    content = A reference to the main feature content.
    """
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='default_feature')
    # ensuring there is a maximum number of 3 steps, with each feature having a unique value.
    step = models.PositiveIntegerField(unique=True, validators = [MaxValueValidator(3)])
    content = models.TextField()

    def __str__(self):
        return f'Feature title: {self.title}'