# Generated by Django 5.0.2 on 2024-03-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_profile_adoption_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_coordinator",
            field=models.BooleanField(default=False),
        ),
    ]
