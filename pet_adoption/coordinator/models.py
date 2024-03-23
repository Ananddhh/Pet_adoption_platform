from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from pets.models import Pet
from django.conf import settings
from pets.models import Pet  

class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='coordinator_adoption_requests')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='coordinator_adoption_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"

class Coordinator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    responsibilities = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

User = get_user_model()

class BookingAppointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
class CoordinatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    responsibilities = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"