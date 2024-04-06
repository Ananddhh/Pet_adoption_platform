from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
# from .views import all_messages
from .views import book_appointment, appointment_success

urlpatterns = [
    # path('all-messages/', all_messages, name='all_messages'),
    path('pets/', views.pet_list, name='pet_list'),
    path('petss/', views.pet_list1, name='pet_list1'),
    # path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('petss/<int:pk>/', views.pet_detail1, name='pet_detail1'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('adoption/', views.adoption_process, name='adoption_process'),
    path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('eventss/<int:event_id>/', views.event_details1, name='event_details1'),
    # path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('lost-found/', views.lost_found_pets, name='lost_found_pets'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('appointment_success/', appointment_success, name='appointment_success'),
    path('adoption-submit/', views.adoption_submit, name='adoption_submit'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    # path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('lost-found/contact/', views.contact_submit_view, name='contact_submit'),
    # path('adoption/process/', views.adoption_process, name='adoption_process'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
