from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('adoption/', views.adoption_process, name='adoption'),
    path('events/<int:event_id>/', views.event_details, name='event_details'),
]

