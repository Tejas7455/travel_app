from django.urls import path
from .views import DestinationAPI

urlpatterns = [
    path('travel/',DestinationAPI.as_view()),
]
