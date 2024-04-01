from django.urls import path
from .views import DestinationAPI,DestinationDetailsAPI

urlpatterns = [
    path('travel/',DestinationAPI.as_view()),
    path('travel/<int:pk>/',DestinationDetailsAPI.as_view()),
]
