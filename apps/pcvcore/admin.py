from django.contrib import admin

from .models import PCVProfile, Teacher, School, UserProfile

admin.site.register(PCVProfile)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(UserProfile)