from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=500)
    points = models.IntegerField()

    def __str__():
        return str(self.name) +": " + str(self.points)
class Mentor(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


