from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STARS = (
    ('★☆☆☆☆', '★☆☆☆☆'),
    ('★★☆☆☆', '★★☆☆☆'),
    ('★★★☆☆', '★★★☆☆'),
    ('★★★★☆', '★★★★☆'),
    ('★★★★★', '★★★★★'),
)

INDUSTRY = (
    ('Agriculture', 'Agriculture'),
    ('Aviation', 'Aviation'),
    ('Business Development', 'Business Development'),
    ('Communications', 'Communications'),
    ('Construction', 'Construction'),
    ('Education', 'Education'),
    ('Energy', 'Energy'),
    ('Engineering', 'Engineering'),
    ('Entertainment', 'Entertainment'),
    ('Fashion', 'Fashion'),
    ('Finance', 'Finance'),
    ('Food', 'Food'),
    ('Government', 'Government'),
    ('Healthcare', 'Healthcare'),
    ('Hospitality', 'Hospitality'),
    ('Human Resources', 'Human Resources'),
    ('Information Technology', 'Information Technology'),
    ('Insurance', 'Insurance'),
    ('Legal', 'Legal'),
    ('Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ('Military', 'Military'),
    ('Transportation', 'Transportation'),
    ('Other', 'Other'),
)


class Scrum(models.Model):
    """
    Represents a Scrum model with Cloudinary fields for document management.

    Attributes:
    title = A reference to the paragraph title.
    image (CloudinaryField) = A field to store an image in Cloudinary.
    There is a default image for fallback purposes.
    updated_on = A reference to the date and time the extract was updated on.
    content = A reference to the main content.
    """
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='default_image')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f'The title of this section is {self.title}'


class Review(models.Model):
    """
    Represents a Review model with Cloudinary fields for document management
    and choice fields for personalisation.

    Attributes:
    author = A registered user who has left a review.
    profile_image (CloudinaryField) = A field to store a user profile image.
        There is a default image for fallback purposes.
    job_industry = A choices field (INDUSTRY) for selecting the reviewer's job.
    rating = A choices field (STARS) for choosing an app rating.
    review = A textfield for the main review content.
    reviewed_on = A reference to the date and time the review was made.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviewer"
    )
    job_industry = models.CharField(
        choices=INDUSTRY,
        default='other',
        max_length=22
    )
    rating = models.CharField(
        choices=STARS,
        default='no rating',
        max_length=5
    )
    review = models.TextField()
    reviewed_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} rated {self.rating} ({self.job_industry})'
