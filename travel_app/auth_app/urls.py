from django.urls import path
from .views import UserRegisterAPI

urlpatterns =[
    path('register/', UserRegisterAPI.as_view()),
]