from django.conf.urls import url
from django.contrib.auth import views as auth_views
from pages import views

urlpatterns = [

        url(r'activities/', views.activities, name ='pages_activities'),
        url(r'hiscore/$', views.hiscore, name = 'pages_hiscore'),
        url(r'hiscore/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.hiscore),
        url(r'new_activity/', views.activity_new, name = 'pages_new_activity'),
        url(r'my_achievements', views.my_achievements, name = 'pages_my_achievements'),
        url(r'del_achievements', views.delete_achievements, name = 'pages_del_achievements'),
        url(r'del_activities', views.delete_activities, name = 'pages_del_activities'),
        url(r'^$', views.index, name = 'pages_index'),
        ]
