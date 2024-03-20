from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)