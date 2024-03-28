from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pets/', blank=True)

    def __str__(self):
        return self.name

class LostItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lost_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class LostPet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='lost_pets/')
    date_lost = models.DateField()

    def __str__(self):
        return self.name

class FoundPet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='found_pets/')
    date_found = models.DateField()

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
    

class AdoptionApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='')
    message = models.TextField()

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name
    


class AdoptionRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Foreign key to the Pet model
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"
    
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"