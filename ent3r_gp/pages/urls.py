from django.conf.urls import url
from django.contrib.auth import views as auth_views
from pages import views

urlpatterns = [

        url(r'activities/', views.activities, name ='pages_activities'),
        url(r'hiscore/', views.hiscore, name = 'pages_hiscore'),
        url(r'new_activity/', views.activity_new, name = 'pages_new_activity'),
        url(r'my_achievements', views.my_achievements, name = 'pages_my_achievements'),
        url(r'^$', views.index, name = 'pages_index'),
        ]
