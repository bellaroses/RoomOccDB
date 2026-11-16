from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id', 'sensor_id', 'occupied', 'time']
        read_only_fields = ['time']
