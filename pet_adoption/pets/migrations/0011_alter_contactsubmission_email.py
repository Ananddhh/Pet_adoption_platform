# Generated by Django 5.0.2 on 2024-03-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0010_remove_contactsubmission_submission_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactsubmission",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
    ]
