from django.contrib import admin
from .models import Pet, LostPet, FoundPet

admin.site.register(LostPet)
admin.site.register(FoundPet)
# admin.site.register(AdoptionApplication)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'available')
    list_filter = ('species', 'breed', 'age', 'available')
    search_fields = ('name', 'breed')
    list_editable = ('available',)
