# Generated by Django 5.0.2 on 2024-03-20 08:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coordinator", "0003_alter_user_groups_alter_user_user_permissions"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
