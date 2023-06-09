"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('EasyLern/', include('EasyLearn.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from EasyLearn.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('EasyLearn.urls')),
    path('auth/', include('djoser.urls')),
    re_path('^auth/ ', include('djoser.urls.authtoken')),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
