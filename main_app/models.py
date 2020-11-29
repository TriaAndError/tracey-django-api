from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()


class TrendingReview(models.Model):
    thumbnail = models.ImageField()
    title = models.CharField(max_length=50)
    context = models.TextField()


class ContactUs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

