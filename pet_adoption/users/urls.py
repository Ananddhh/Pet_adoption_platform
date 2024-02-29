from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='register'),
    path('settings/', views.user_settings, name='user_settings'),
    path('<str:username>/', views.user_profile, name='user_profile'),
    # Other URL patterns...
]
