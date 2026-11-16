from django.shortcuts import render
from rest_framework import viewsets

from .models import Room
from .serializers import RoomSerializer


def index(request):
    return render(request, 'occ_db/index.html', {})


class RoomViewSet(viewsets.ModelViewSet):
    """
    GET    /rooms/            list all rooms
    POST   /rooms/            create a room
    GET    /rooms/<room_id>/  one room
    PUT    /rooms/<room_id>/  update a room
    DELETE /rooms/<room_id>/  delete a room
    """
    queryset = Room.objects.all().order_by('room_id')
    serializer_class = RoomSerializer
    lookup_field = 'room_id'
