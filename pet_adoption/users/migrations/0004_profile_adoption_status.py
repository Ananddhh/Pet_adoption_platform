# Generated by Django 5.0.2 on 2024-03-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="adoption_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]
