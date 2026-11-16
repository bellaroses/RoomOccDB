from django.db import models


class Room(models.Model):
    # One row per study room: the latest status reported by its sensor.
    room_id = models.IntegerField(unique=True)
    sensor_id = models.IntegerField()
    occupied = models.BooleanField(default=False)
    # Set by the server every time the row is saved. Sensors don't send it.
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.room_id} ({'occupied' if self.occupied else 'vacant'})"
