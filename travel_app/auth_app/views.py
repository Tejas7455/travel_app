from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer

class UserRegisterAPI(CreateAPIView):
    serializer_class = UserSerializer