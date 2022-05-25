from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Comment(models.Model):
#     ratePost = models.IntegerField()
#     comment = models.TextField()

class Type(models.Model):
    foodPost = models.ForeignKey(User, related_name = 'foodPost', on_delete=models.CASCADE)
    foodType = models.CharField(max_length = 50, default='dessert')
    foodName = models.CharField(max_length=50)
    foodRate = models.IntegerField()

    def __str__(self):
        foodName = "Name: " + self.foodName + ", Type of Food: " + self.foodType + ", Rating: " + str(self.foodRate) + "stars out of 10"
        return foodName

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
#    image = models.ImageField(default = 'default.jpg')
    location = models.CharField(max_length=100)
    qualifications = models.TextField()
