from django.contrib import admin
from django.contrib import admin
from .models import Pet, LostItem, LostPet, FoundPet, Appointment, AdoptionApplication, AdoptionRequest, ContactSubmission

# Register your models here

admin.site.register(LostItem)
admin.site.register(LostPet)
admin.site.register(FoundPet)
admin.site.register(Appointment)

#if the model is already registered
if admin.site.is_registered(AdoptionApplication):
    # Unregister the model from the existing custom admin class
    admin.site.unregister(AdoptionApplication)

# Register the model without any custom admin class
admin.site.register(AdoptionApplication)
admin.site.register(AdoptionRequest)
admin.site.register(ContactSubmission)
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'available')
    list_filter = ('species', 'breed', 'age', 'available')
    search_fields = ('name', 'breed')
    list_editable = ('available',)
