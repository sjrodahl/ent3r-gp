from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account import views

urlpatterns= [
        url(r'login/',
            views.login,
            {'template_name': 'account/login.html'},
            name = 'login'),
        url(r'logout/',
            auth_views.logout,
            {'template_name': 'account/logout.html'},
            name= 'logout'),
        url(r'^password-change-done/$',
            auth_views.password_change_done,
            {'template_name': 'account/password_change_done.html'},
            name='password_change_done'
            ),
        url(r'^password-change/$',
            auth_views.password_change,
            {'post_change_redirect': 'password_change_done',
            'template_name': 'account/password_change.html'},
            name='password_change'
            ),
        url(r'^$', views.index, name='account_index'),
        ]
