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
    
    def post(self, request):
        serializer = DestinationSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)