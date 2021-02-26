from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from User.serializer import ProfileSerializer, ProfileDetailSerializer
from User.models import Profile

# from rest_framework.pagination import PageNumberPagination

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


# Create your views here.
class CreateUser(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class ProfileDetail(generics.RetrieveAPIView):
    serializer_class = ProfileDetailSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        try:
            return Profile.objects.get(identifier=self.kwargs['profile'])
        except Exception:
            raise NotFound(detail="Profile does not exist.")


class ListAllProfiles(generics.ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        query_profile = Profile.objects.all()
        serial_profile = ProfileDetailSerializer(query_profile, many=True)
        return Response(serial_profile.data)
