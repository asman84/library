from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import UserCreateSerializer


# Create your views here.
class UserCreateAPIVIew(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
