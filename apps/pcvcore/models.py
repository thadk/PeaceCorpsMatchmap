from django.db import models
from apps.worldmap import data_options

# Create your models here.
class PCVProfile(models.Model):
    country = models.CharField(choices=data_options.COUNTRIES, max_length=128)
    sector = models.CharField(choices=data_options.SECTORS, max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()

class Teacher(models.Model):
    school = models.CharField(max_length=128)
    grade = models.CharField(max_length=5)
    following = models.ForeignKey('auth.User')

class School(models.Model):
    city = models.CharField(max_length=128)
    state = models.CharField(choices=data_options.STATES, max_length=128)
    school_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)
    about = models.TextField()

class UserProfile(models.Model):
    is_pcv = models.BooleanField()
    address = models.CharField(max_length=128)
    bio = models.TextField()
