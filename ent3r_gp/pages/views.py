from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import NewActivityForm
from .models import Mentor, Activity, Achievement


def index(request):
    return HttpResponse("Hello ENT3R")
     #return render("Hello")

@login_required
def hiscore(request):
    mentors = Mentor.objects.all()
    users = User.objects.all()
    achievements = Achievement.objects.all()
    my_achs  = Achievement.objects.filter(user_id=request.user.id)
    my_score = 0
    for a in my_achs:
        my_score += a.activity.points

    print(request.user.get_username()+"'s score: " + str( my_score))
    return render(request, 'pages/highscore.html', {'m': mentors, 'u': users, 'a': achievements, 's':my_score})

@login_required
def activities(request):
    act = Activity.objects.all()
    return render(request, 'pages/activities.html', {'act': act})

@login_required
def activity_new(request):
    if request.method=="POST":
        form = NewActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
        return redirect('pages_hiscore')
    else:
        form = NewActivityForm()
        return render(request, 'pages/activity_new.html', {'form': form})

