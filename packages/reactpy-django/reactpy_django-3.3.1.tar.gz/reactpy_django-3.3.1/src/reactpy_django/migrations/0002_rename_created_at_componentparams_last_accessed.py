# Generated by Django 4.1.5 on 2023-01-11 01:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reactpy_django", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="componentparams",
            old_name="created_at",
            new_name="last_accessed",
        ),
    ]
