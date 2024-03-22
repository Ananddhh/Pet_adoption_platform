from django.urls import path
from . import views
from users.views import user_register , user_login
from .views import contact_submit_view

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('faq/', views.faq_page, name='faq'),
    path('contact_submit/', contact_submit_view, name='contact_submit'),
    path('register/', user_register, name='user_register'),
    path('login/',views.user_login, name = 'user_login'),
    path('adoption_event/', views.adoption_event, name = 'adoption_event'),
    path('coordinator-dashboard/', views.coordinator_dashboard, name='coordinator_dashboard'),
 ]
   
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('about/', views.about_page, name='about'),
#     path('contact/', views.contact_page, name='contact'),
#     path('faq/', views.faq_page, name='faq'),
#     path('contact_submit/', views.contact_submit_view, name='contact_submit'),
#     path('adoption_event/', views.adoption_event, name='adoption_event'),
# ]
