# Generated by Django 4.2.11 on 2024-06-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0002_alter_review_reviewed_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrum',
            name='image',
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=120),
        ),
    ]
