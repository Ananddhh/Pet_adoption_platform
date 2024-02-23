from django.urls import path
from . import views
from .views import contact_page,contact_submit_view

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('faq/', views.faq_page, name='faq'),
    path('contact_submit/', contact_submit_view, name='contact_submit'),
]
    # Add more URL patterns for other core features as needed
