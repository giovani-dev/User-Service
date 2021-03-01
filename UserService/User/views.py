from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from User.serializer import ProfileSerializer, ProfileDetailSerializer
from User.models import Profile

from util import base_view

import json


class CreateUser(base_view.CreateView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]


class ListAllProfiles(base_view.ListAllView):
    permission_classes = [AllowAny]
    serializer_class = ProfileDetailSerializer
    QUERY = Profile.objects.filter(login__is_active=False).order_by('-registration_date')


class ProfileDetail(base_view.GetUpdateDestroyView):
    serializer_class = ProfileDetailSerializer
    permission_classes = [AllowAny]
    CACHE = True
    MODEL = Profile
    SLUG_TAG = 'profile'
    ERROR_MSG_QUERY_DOES_NOT_EXIST = "Profile does not exist."