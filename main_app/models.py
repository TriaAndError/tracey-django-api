from django.db import models



class Registration(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()


class Booking(models.Model):   # missing details
    pass


