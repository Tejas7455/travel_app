from rest_framework import serializers
from .models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'