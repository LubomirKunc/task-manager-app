# Generated by Django 5.0.2 on 2024-04-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tasks_created',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='tasks_deleted',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
