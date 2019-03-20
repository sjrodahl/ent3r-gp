from django.urls import path, include
from django.contrib import admin

from pages import views as pages_views

urlpatterns = [
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
