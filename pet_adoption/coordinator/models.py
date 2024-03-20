from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Coordinator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    responsibilities = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# models.py

User = get_user_model()

class AdoptionApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields for AdoptionApplication model
    pet_name = models.CharField(max_length=100)
    reason_for_adoption = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields for ContactMessage model
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields for Appointment model
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

class CoordinatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    responsibilities = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username