# Generated by Django 4.2.11 on 2024-05-02 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0003_alter_workspace_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('notes', models.TextField(null=True)),
                ('status', models.TextField(choices=[('TO-DO', 'To Do'), ('IN-PROGRESS', 'In Progress'), ('DONE', 'Completed')], default='TO-DO')),
                ('priority', models.TextField(choices=[('CRITICAL', 'Critical'), ('MAJOR', 'Major'), ('MINOR', 'Minor'), ('NICE-TO-HAVE', 'Nice to have!')], default='minor')),
                ('due_date', models.DateTimeField(auto_now=True)),
                ('updated', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_creator', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]