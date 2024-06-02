# workshop/models.py

from django.db import models

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
