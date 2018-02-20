from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'activities/', views.activities, name ='pages_activities'),
    url(r'hiscore/', views.hiscore, name = 'pages_hiscore'),
    url(r'^$', views.index, name = 'pages_index'),
]
