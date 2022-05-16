from django.db import models

# Create your models here.

class FoodType(models.Model):
    types = (
        ('p', 'protein'),
        ('c', 'carbohydrates'),
        ('l', 'lipids'),
    )
    name = models.CharField(max_length=50)
    log = models.CharField(max_length=50, choices=types)

    def __str__(self):
        return self.name


class Type(models.Model):
    types = models.ManyToManyField(FoodType)
    foodType = models.CharField(max_length=50)
    totalCal = models.IntegerField(blank=True)

    def __str__(self):
        return self.foodType
