from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class MentorPair(models.Model):
    name = models.CharField(max_length=30)
    mentor_1 = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentorpair1')
    mentor_2 = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentorpair2')

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=500)
    points = models.IntegerField()
    tag = models.CharField(max_length=50)
    completed_by = models.ManyToManyField(Mentor, through='Achievement')

    def __str__(self):
        return str(self.tag) + ':' + str(self.points)


class Achievement(models.Model):
    user = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.activity) + ':' + self.date_added.strftime('%d-%m-%y')


