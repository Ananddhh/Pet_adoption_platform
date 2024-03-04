from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from pets.models import AdoptionApplication

class AdoptionApplicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:  
            qs = qs.none()
        return qs

admin.site.register(AdoptionApplication, AdoptionApplicationAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
