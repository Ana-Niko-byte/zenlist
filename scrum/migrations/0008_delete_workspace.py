# Generated by Django 4.2.11 on 2024-04-20 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0007_alter_review_reviewed_on_workspace'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Workspace',
        ),
    ]
