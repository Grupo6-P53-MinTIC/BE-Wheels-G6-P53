from rest_framework import serializers
from authApp.models import Travel


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ['id', 'id_manager', 'from_place', 'to_place',
                  'pass_through', 'published', 'date_travel', 'seats', 'price']
