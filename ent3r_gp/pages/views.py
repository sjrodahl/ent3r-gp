from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import NewActivityForm
from .models import Mentor, Activity


def index(request):
    return HttpResponse("Hello ENT3R")
     #return render("Hello")

def hiscore(request):
    mentors = Mentor.objects.all()
    return render(request, 'pages/highscore.html', {'m': mentors})

def activities(request):
    return render(request, 'pages/activities.html', {})

def activity_new(request):
    if request.method=="POST":
        form = NewActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
        return redirect('pages_hiscore')
    else:
        form = NewActivityForm()
        return render(request, 'pages/activity_new.html', {'form': form})

