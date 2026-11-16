from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'sensor_id', 'occupied', 'time')
