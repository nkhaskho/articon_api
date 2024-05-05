from django.db import models

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

    def __str__(self):
        return self.name