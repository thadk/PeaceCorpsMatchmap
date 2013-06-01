from django.db import models
from apps.worldmap import data_options

# Create your models here.
class PCVProfile(models.Model):
    country = models.CharField(choice=data_options.COUNTRIES)
    sector = models.CharField(choices=data_options.SECTORS)
    startDate = models.DateField()
    endDate = models.DateField()

class Teacher(models.Model):
    school = models.CharField(max_length=128)
    grade = models.CharField(max_length=5)
    
