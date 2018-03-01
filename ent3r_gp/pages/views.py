from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Sum
from .forms import NewActivityForm
from .models import Mentor, Activity, Achievement
from django.contrib.auth import views as auth_views

def index(request):
    return HttpResponse("Hello ENT3R")
     #return render("Hello")

@login_required
def hiscore(request):
    hiscorelist = Achievement.objects.values('user__username').annotate(score=Sum('activity__points'))
    return render(request, 'pages/highscore.html', {'qs': hiscorelist})

@login_required
def activities(request):
    act = Activity.objects.all()
    if request.method == "POST":
        checked = request.POST.getlist('choices')
        for ach in checked:
            completed__activity = Activity.objects.get(id=ach)
            new_achievement = Achievement.objects.create(activity=completed__activity, user = request.user)
            new_achievement.save()
        return redirect('pages_hiscore')
    else:
        return render(request, 'pages/activities.html', {'act': act })

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

@login_required
def my_achievements(request):
    my_achievements = Achievement.objects.filter(user_id = request.user.id)
    print(request.user.id)
    for i in my_achievements:
        print(i.user.username)
    return render(request, 'pages/my_achievements.html', {'my_ach': my_achievements})

