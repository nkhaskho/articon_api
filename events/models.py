from django.db import models

from users.models import User

# Create your models here.

EVENT_CHOICES = [
    ("commercial", "Commercial"),
    ("sejnen", "Sejnen"),
    ("region", "Region"),
    ("handicape", "Handicapé"),
    ("nouveau artisan", "Nouveau Artisan")
]

class Event(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55, choices=EVENT_CHOICES)
    description = models.TextField(max_length=512)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    video = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name} [{self.date}]'
    

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'User{self.user} Event{self.date}'
