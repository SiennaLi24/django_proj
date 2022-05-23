from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Type(models.Model):
    types = [
        ('d', 'dessert'),
        ('m', 'main course'),
        ('a', 'appetizer'),
    ]
    foodPost = models.ForeignKey(User, related_name = 'foodPost', on_delete=models.CASCADE)
    foodType = models.CharField(max_length = 50, choices = types, default='dessert')
    foodName = models.CharField(max_length=50)
    foodRate = models.IntegerField(blank = True)

    def __str__(self):
        return self.foodName

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
