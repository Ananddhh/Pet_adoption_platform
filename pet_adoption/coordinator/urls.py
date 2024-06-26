from django.urls import path
from . import views
from .views import all_messages,adoption_requests

urlpatterns = [
    path('manage_adoption_applications/', views.manage_adoption_applications, name='manage_adoption_applications'),
    path('update_request_status/<int:application_id>/', views.update_request_status, name='update_request_status'),
    path('view_user_messages/', views.view_user_messages, name='view_user_messages'),
    path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
    path('coordinator_profile/', views.coordinator_profile, name='coordinator_profile'),
    path('update_coordinator_profile/', views.update_coordinator_profile, name='update_coordinator_profile'),
    path('coordinator-register/', views.coordinator_register, name='coordinator_register'),
    path('coordinator-login/', views.coordinator_login, name='coordinator_login'),
    path('all-messages/', all_messages, name='all_messages'),
    path('adoption_req/', adoption_requests, name='adoption_req'),
    path('coord_logout/', views.coordinator_logout, name='coord_logout'),
    path('set_coordinator_credentials/', views.set_coordinator_credentials, name='set_coordinator_credentials'),
]

