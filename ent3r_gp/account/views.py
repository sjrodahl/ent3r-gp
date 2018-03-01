from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

@login_required
def index(request):
    return render(request, 'account/index.html')

def login(request, **kwargs):
    if (request.user.is_authenticated):
        return redirect('pages_hiscore')
    else:
        return auth_views.login(request, **kwargs)
