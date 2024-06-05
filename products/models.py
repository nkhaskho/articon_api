from django.db import models
from django.utils import timezone

from users.models import User 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0, null=True)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    artisan = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(0, (5))])
    created_at = models.DateTimeField(default=timezone.now)
