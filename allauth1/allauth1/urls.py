"""
URL configuration for allauth1 project.

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
from dashboard import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path("accounts/profile/", views.profile, name='profile'),
    path("google-auth/", include('google_auth.urls', namespace='google_auth')),
]
