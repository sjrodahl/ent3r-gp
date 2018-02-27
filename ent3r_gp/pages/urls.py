from django.conf.urls import url
from django.contrib.auth import views as auth_views
from pages import views

urlpatterns = [
        url(r'login/',
            views.login,
            {'template_name': 'pages/login.html'},
            name = 'login'),
        url(r'logout/',
            auth_views.logout,
            {'template_name': 'pages/logout.html'},
            name= 'logout'),
        url(r'^password-change-done/$',
            auth_views.password_change_done,
            {'template_name': 'pages/password_change_done.html'},
            name='password_change_done'
            ),
        url(r'^password-change/$',
            auth_views.password_change,
            {'post_change_redirect': 'password_change_done',
            'template_name': 'pages/password_change.html'},
            name='password_change'
            ),
        url(r'activities/', views.activities, name ='pages_activities'),
        url(r'hiscore/', views.hiscore, name = 'pages_hiscore'),
        url(r'^$', views.index, name = 'pages_index'),
        url(r'new_activity/', views.activity_new, name = 'pages_new_activity'),
        url(r'my_achievements', views.my_achievements, name = 'pages_my_achievements'),
        ]
