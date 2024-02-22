from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.email

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'Testimonial by {self.author}'
