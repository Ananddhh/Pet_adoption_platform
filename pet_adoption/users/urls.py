from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('', views.homepage, name='homepage'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.custom_logout, name='logout'),
    path('settings/', views.user_settings, name='user_settings'),
    path('submit-adoption-request/', views.submit_adoption_request, name='submit_adoption_request'),
    path('submit-contact-message/', views.submit_contact_message, name='submit_contact_message'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    # Other URL patterns...
]
# from django.urls import path
# from . import views

    # path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # path('<str:username>/', views.user_profile, name='user_profile'),
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='user_login'),
#     path('logout/', views.custom_logout, name='logout'),
#     path('register/', views.user_register, name='register'),
#     path('settings/', views.user_settings, name='user_settings'),
#     path('profile/<str:username>/', views.user_profile, name='user_profile'),
# ]
