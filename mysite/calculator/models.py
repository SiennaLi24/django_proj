from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.


class Type(models.Model):
    foodPost = models.ForeignKey(User, related_name = 'foodPost', on_delete=models.CASCADE)
    foodType = models.CharField(max_length = 50, default='dessert')
    foodName = models.CharField(max_length=50)
    foodRate = models.IntegerField()

    def __str__(self):
        foodName = "Name: " + self.foodName + ", Type of Food: " + self.foodType + ", Rating: " + str(self.foodRate) + "stars out of 10"
        return foodName


class Comment(models.Model):
    post = models.ForeignKey(Type, on_delete=models.CASCADE)
    ratePost = models.IntegerField()
    comment = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
         return self.comment

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
#    image = models.ImageField(default = 'default.jpg')
    location = models.CharField(max_length=100)
    qualifications = models.TextField()
