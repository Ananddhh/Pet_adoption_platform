from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/',views.user_register, name = 'user_register'),
    # path('admin/login/', views.admin_login, name='admin_login'),
    # path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('coordinator_home/',views.coordinator_home,name = 'coordinator_home'),
    path('coordinator_login/',views.coordinator_login,name = 'coordinator_login '),
]