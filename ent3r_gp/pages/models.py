from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=500)
    points = models.IntegerField()

class Mentor(models.Model):
    name = CharField(max_length = 100)
    email = EmailField(unique=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    activities = models.ManyToManyField(Activity)


