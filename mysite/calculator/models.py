from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from PIL import Image

# Create your models here.


class Type(models.Model):

    foodPost = models.ForeignKey(
        User,
        related_name = 'foodPost',
        on_delete=models.CASCADE
    )

    DESSERT = 'dessert'
    MAIN_COURSE = 'main course'
    APPETIZER = 'appetizer'
    FOOD_CHOICES = [
        (DESSERT, 'Dessert'),
        (MAIN_COURSE, 'Main Course'),
        (APPETIZER, 'Appetizer'),
    ]
    foodType = models.CharField(
        max_length = 50,
        choices = FOOD_CHOICES,
        default = DESSERT,
    )
    foodName = models.CharField(max_length=50)
    ONE = '1 star'
    TWO = '2 stars'
    THREE = '3 stars'
    FOUR = '4 stars'
    FIVE = '5 stars'
    SIX = '6 stars'
    SEVEN = '7 stars'
    EIGHT = '8 stars'
    NINE = '9 stars'
    TEN = '10 stars'
    STAR_CHOICES = [
        (ONE, 'One star'),
        (TWO, 'Two stars'),
        (THREE, 'Three stars'),
        (FOUR, 'Four stars'),
        (FIVE, 'Five stars'),
        (SIX, 'Six stars'),
        (SEVEN, 'Seven stars'),
        (EIGHT, 'Eight stars'),
        (NINE, 'Nine stars'),
        (TEN, 'Ten stars'),
    ]
    foodRate = models.CharField(
        max_length=20,
        choices = STAR_CHOICES,
        default = ONE,
    )

    foodComment = models.TextField(default = "")

    foodImage = models.ImageField(default='food_pics/blank.jpeg', upload_to='food_pics')

    def __str__(self):
        foodName = "Name: " + self.foodName + ", Type of Food: " + self.foodType + ", Rating: " + str(self.foodRate) + "stars out of 10"
        return foodName

    def save(self):
            super().save()
            img = Image.open(self.foodImage.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.foodImage.path)

class Comment(models.Model):
    post = models.ForeignKey(Type, on_delete=models.CASCADE)
    ONE = '1 star'
    TWO = '2 stars'
    THREE = '3 stars'
    FOUR = '4 stars'
    FIVE = '5 stars'
    SIX = '6 stars'
    SEVEN = '7 stars'
    EIGHT = '8 stars'
    NINE = '9 stars'
    TEN = '10 stars'
    STAR_CHOICES = [
        (ONE, 'One star'),
        (TWO, 'Two stars'),
        (THREE, 'Three stars'),
        (FOUR, 'Four stars'),
        (FIVE, 'Five stars'),
        (SIX, 'Six stars'),
        (SEVEN, 'Seven stars'),
        (EIGHT, 'Eight stars'),
        (NINE, 'Nine stars'),
        (TEN, 'Ten stars'),
    ]
    ratePost = models.CharField(
        max_length = 50,
        choices = STAR_CHOICES,
        default = ONE
    )
    comment = models.TextField(default = "")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
         return self.comment



class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key = True
    )
    image = models.ImageField(default='profile_pics/profile.jpeg', upload_to='profile_pics')
    location = models.CharField(max_length=100, default = "")
    qualifications = models.TextField(default = "")
    def save(self):
            super().save()
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
