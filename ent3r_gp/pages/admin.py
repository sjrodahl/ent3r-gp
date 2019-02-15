from django.contrib import admin

from .models import Activity, Achievement, MentorPair
# Register your models here.

admin.site.register(MentorPair)
admin.site.register(Activity)
admin.site.register(Achievement)

