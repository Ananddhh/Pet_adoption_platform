# Generated by Django 5.0.2 on 2024-04-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_userprofile_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="admin_reply",
            field=models.TextField(blank=True),
        ),
    ]
