from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('adoption/', views.adoption_process, name='adoption_process'),
    # path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('lost-found/', views.lost_found_pets, name='lost_found_pets'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('adoption-submit/', views.adoption_submit, name='adoption_submit'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('lost-found/contact/', views.contact_submit_view, name='contact_submit'),
    # path('adoption/process/', views.adoption_process, name='adoption_process'),
    ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('pets/', views.pet_list, name='pet_list'),
#     path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
#     path('adoption/', views.adoption_process, name='adoption_process'),
#     path('lost-found/', views.lost_found_pets, name='lost_found_pets'),
#     path('book-appointment/', views.book_appointment, name='book_appointment'),
#     path('adoption-submit/', views.adoption_submit, name='adoption_submit'),
#     path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
#     path('lost-found/contact/', views.contact_submit_view, name='contact_submit'),
# ]
