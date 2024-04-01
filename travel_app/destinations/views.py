from rest_framework.views import APIView
from .models import Destination
from .serializers import DestinationSerializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DestinationAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


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
    
class DestinationDetailsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk=None):
        obj = get_object_or_404(Destination, pk=pk)
        serializer = DestinationSerializers(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        obj = get_object_or_404(Destination,pk=pk)
        serializer = DestinationSerializers(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        obj = get_object_or_404(Destination, pk=pk)
        serializer = DestinationSerializers(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        obj = get_object_or_404(Destination, pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

    
    