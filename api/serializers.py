from rest_framework import serializers
from .models import HouseDetails


class HouseDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = HouseDetails
        fields = ('id','name', 'date_created', 'date_modified','power_consumption')
        read_only_fields = ('date_created', 'date_modified')
