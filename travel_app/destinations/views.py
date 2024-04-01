from rest_framework.views import APIView
from .models import Destination
from .serializers import DestinationSerializers
from rest_framework.response import Response
from rest_framework import status

class DestinationAPI(APIView):
    def get (self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializers(destinations, many =True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)