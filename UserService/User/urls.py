"""UserService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import  User.views as vw_user

urlpatterns = [
    path('register', vw_user.CreateUser.as_view(), name='user_registration'),
    path('detail/<slug:profile>', vw_user.ProfileDetail.as_view(), name='profile_detail'),
    path('list', vw_user.ListAllProfiles.as_view(), name='list_all_profiles'),
]
