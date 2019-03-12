from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account import views

urlpatterns= [
        url(r'login/',
            views.LoginView.as_view(),
            {'template_name': 'account/login.html'},
            name = 'login'),
        url(r'logout/',
            views.LogoutView.as_view(),
            {'template_name': 'account/logout.html'},
            name= 'logout'),
        url(r'^password-change-done/',
            auth_views.PasswordChangeDoneView.as_view(),
            {'template_name': 'account/password_change_done.html'},
            name='password_change_done'
            ),
        url(r'^password-change/$',
            auth_views.PasswordChangeView.as_view(),
            {'post_change_redirect': 'password_change_done',
            'template_name': 'account/password_change.html'},
            name='password_change'
            ),
        url(r'^$', views.index, name='account_index'),
        ]
