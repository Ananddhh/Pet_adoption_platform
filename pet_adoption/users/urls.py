from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.custom_logout, name='logout'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-profile/', views.admin_profile, name='admin_profile'),
    path('update-status/<int:form_id>/<str:new_status>/', views.update_status, name='update_status'),
    path('register/', views.user_register, name='register'),
    path('settings/', views.user_settings, name='user_settings'),
    # path('<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # Other URL patterns...
]
