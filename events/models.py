from django.db import models

# Create your models here.

EVENT_CHOICES = [
    ("type1", "Type 1"),
    ("type2", "Type 2")
]

class Event(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55, choices=EVENT_CHOICES)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name} [{self.date}]'
