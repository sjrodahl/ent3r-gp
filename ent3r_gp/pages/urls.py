from django.conf.urls import url
from django.contrib.auth import views as auth_views
from pages import views

urlpatterns = [
    url(r'login/',
        auth_views.login,
        {'template_name': 'pages/login.html'},
        name = 'login'),
    url(r'logout/',
        auth_views.logout,
        {'template_name': 'pages/logout.html'},
        name= 'logout'),
    url(r'activities/', views.activities, name ='pages_activities'),
    url(r'hiscore/', views.hiscore, name = 'pages_hiscore'),
    url(r'^$', views.index, name = 'pages_index'),
    url(r'new_activity/', views.activity_new, name = 'pages_new_activity')
]
