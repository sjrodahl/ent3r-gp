from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

@login_required
def index(request):
    return render(request, 'account/index.html')

class LoginView(auth_views.LoginView):
    template_name = 'account/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'
