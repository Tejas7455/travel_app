from django.urls import path
from .views import DestinationAPI,destinationDetailsAPI

urlpatterns = [
    path('travel/',DestinationAPI.as_view()),
    path('travel/<int:pk>/',destinationDetailsAPI.as_view()),
]
