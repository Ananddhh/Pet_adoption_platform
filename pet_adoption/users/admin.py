from django.contrib import admin
from .models import CustomUser, UserProfile

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_regular_user']  # Customize the fields displayed in the admin list view

admin.site.register(CustomUser, CustomUserAdmin)  # Register CustomUser model with the customized admin interface

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'adoption_status']  # Customize the fields displayed in the admin list view

admin.site.register(UserProfile, UserProfileAdmin)  # Register UserProfile model with the customized admin interface
