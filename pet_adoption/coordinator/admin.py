from django.contrib import admin
from .models import CoordinatorProfile, AdoptionApplication, ContactMessage, Appointment

admin.site.register(CoordinatorProfile)
admin.site.register(AdoptionApplication)
admin.site.register(ContactMessage)
admin.site.register(Appointment)
