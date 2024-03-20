from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('manage_adoption_applications/', views.manage_adoption_applications, name='manage_adoption_applications'),
    path('update_request_status/<int:application_id>/', views.update_request_status, name='update_request_status'),
    path('view_user_messages/', views.view_user_messages, name='view_user_messages'),
    path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
    path('coordinator_profile/', views.coordinator_profile, name='coordinator_profile'),
    path('update_coordinator_profile/', views.update_coordinator_profile, name='update_coordinator_profile'),
    path('coordinator-register/', views.coordinator_register, name='coordinator_register'),
    path('coordinator-login/', views.coordinator_login, name='coordinator_login'),
]

# urlpatterns = [
#     path('coordinator-register/', views.coordinator_register, name='coordinator_register'),
#     path('coordinator-login/', views.coordinator_login, name='coordinator_login'),
#     path('dashboard/', views.coordinator_dashboard, name='coordinator_dashboard'),
# ]