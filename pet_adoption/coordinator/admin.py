from django.contrib import admin
from django.contrib import admin
from .models import Coordinator
from pets.models import  AdoptionRequest, ContactSubmission

from .models import CoordinatorProfile,BookingAppointment
# AdoptionApplication, ContactMessage,

admin.site.register(Coordinator)
admin.site.register(CoordinatorProfile)
# admin.site.register(AdoptionApplication)
# admin.site.register(ContactMessage)
# admin.site.register(Appointment)
from .models import BookingAppointment, AdoptionRequest, ContactSubmission

@admin.register(BookingAppointment)
class BookingAppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time')
    search_fields = ('name', 'email')
    list_filter = ('date', 'time')

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'status')
    search_fields = ('user__username', 'pet__name')
    list_filter = ('status',)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')