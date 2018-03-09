from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=500)
    points = models.IntegerField()
    tag = models.CharField(max_length=50)
    completed_by = models.ManyToManyField(User, through='Achievement')
    def __str__(self):
        return str(self.name) +": " + str(self.points)

class Achievement(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    date_added = models.DateTimeField(auto_now_add = True)

class Mentor(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

