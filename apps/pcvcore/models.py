from django.db import models
from apps.worldmap import data_options

# Create your models here.
class PCVProfile(models.Model):
    country = models.CharField(choice=data_options.COUNTRIES)
    sector = models.CharField(choices=data_options.SECTORS)
    start_date = models.DateField()
    end_date = models.DateField()

class Teacher(models.Model):
    school = models.CharField(max_length=128)
    grade = models.CharField(max_length=5)
    following = models.ForeignKey('auth.User')

class School(models.Model):
    city = models.CharField(max_length=128)
    state = models.CharField(choices=data_options.STATES)
    school_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)
    about = models.CharField()

class UserProfile(models.Model):
    is_pcv = models.BooleanField()
    address = models.CharField()
    bio = modles.CharField()
