# Generated by Django 4.2.11 on 2024-06-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_remove_task_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]