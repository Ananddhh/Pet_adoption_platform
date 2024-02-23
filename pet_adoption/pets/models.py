from django.db import models

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