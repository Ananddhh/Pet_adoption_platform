from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile, name='user_profile'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('settings/', views.user_settings, name='user_settings'),
]
