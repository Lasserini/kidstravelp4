from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CATEGORY = (("museum", "Museum"), ("monument", "Monument"), ("park", "Park"),
            ("day_trip", "Day Trip"), ("sports", "Sports"), ("cafe", "Cafe"),
            ("restaurant", "Restaurant"), ("culture", "Cultural"),
            ("playground", "Playground"), ("activity", "Activity"))
PRICE = ((0, "Free"), (1, "Costs Money"))
CITY = (("copenhagen", "Copenhagen"), ("florence", "Florence"))
RATING = ((1, "*"), (2, "**"), (3, "***"), (4, "****"), (5, "*****"))


# Model for experiences
class Experience(models.Model):

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    city = models.TextField(choices=CITY)
    category = models.TextField(choices=CATEGORY)
    description = models.TextField()
    excerpt = models.TextField()
    price = models.IntegerField(choices=PRICE, default=1)
    directions = models.URLField(max_length=400, blank=True)
    website = models.URLField(max_length=400, blank=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='experience_like', blank=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


# Model for Reviews
class Review(models.Model):

    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=50)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=RATING, default=5)
    likes = models.ManyToManyField(
        User, related_name='review_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review {self.content} by {self.username}"

    def number_of_likes(self):
        return self.likes.count()
