from django.urls import path, register_converter
from django.contrib.auth import views as auth_views

from pages import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.OneOrTwoDigitMonthConverter, 'mm')

urlpatterns = [

        path('activities/', views.activities, name='pages_activities'),
        path('hiscore/', views.hiscore, name='pages_hiscore'),
        path('hiscore/<yyyy:year>/<mm:period>/', views.hiscore),
        path('hiscore/total/', views.hiscore_total, name='pages_hiscore_total'),
        path('new_activity/', views.activity_new, name='pages_new_activity'),
        path('my_achievements/', views.my_achievements, name='pages_my_achievements'),
        path('del_achievements/', views.delete_achievements, name='pages_del_achievements'),
        path('del_activities/', views.delete_activities, name='pages_del_activities'),
        path('', views.index, name='pages_index'),
        ]
