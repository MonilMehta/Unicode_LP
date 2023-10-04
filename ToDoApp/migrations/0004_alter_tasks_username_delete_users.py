# Generated by Django 4.2 on 2023-10-03 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ToDoApp", "0003_alter_tasks_description_alter_tasks_taskname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="username",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]
