from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MentorPair(models.Model):
    name = models.CharField(max_length=30)
    mentor_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorpair1')
    mentor_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorpair2')

    def __str__(self):
        return(self.name)

class Activity(models.Model):
    name = models.CharField(max_length=500)
    points = models.IntegerField()
    tag = models.CharField(max_length=50)
    completed_by = models.ManyToManyField(User, through='Achievement')

    def __str__(self):
        return str(self.tag) +":" + str(self.points)

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True)

class Mentor(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

