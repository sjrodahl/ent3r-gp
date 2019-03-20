import logging

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

logger = logging.getLogger('ent3r_gp.'+__name__)

@login_required
def index(request):
    return render(request, 'account/index.html')

class LoginView(auth_views.LoginView):
    template_name = 'account/login.html'


    def form_invalid(self, form):
        username = form['username'].value()
        logger.debug('Failed log-in attempt: Username: ' + username)
        return super().form_invalid(form)


class LogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'
