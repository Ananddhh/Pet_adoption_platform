"""
URL configuration for pet_adoption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
  # custom authentication views

urlpatterns = [
    # path('admin/login/', auth_views.admin_login, name='admin_login'),  # Custom admin login URL
    path('admin/', admin.site.urls),  # Django administration URLs
    path('', include('core.urls')),  # Include core app URLs
    path('', include('pets.urls')),  # Include pets app URLs
    path('', include('coordinator.urls')),  # Include coordinator app URLs
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
