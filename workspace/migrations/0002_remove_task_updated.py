# Generated by Django 4.2.11 on 2024-06-10 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='updated',
        ),
    ]