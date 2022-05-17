from django.db import models

# Create your models here.


class TotalToday(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Type(models.Model):
    types = [
        ('p', 'protein'),
        ('c', 'carbohydrates'),
        ('l', 'lipids'),
    ]
    name = models.CharField(max_length = 13, choices = types, default='protein')
    foodType = models.CharField(max_length=50)
    totalCal = models.IntegerField(blank=True)

    def __str__(self):
        return self.foodType
