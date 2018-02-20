from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello ENT3R")
     #return render("Hello")

def hiscore(request):
    return render(request, 'pages/highscore.html', {})

def activities(request):
    return render(request, 'pages/activities.html', {})
