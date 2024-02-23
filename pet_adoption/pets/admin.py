from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'available')
    list_filter = ('species', 'breed', 'age', 'available')
    search_fields = ('name', 'breed')
    list_editable = ('available',)
    
