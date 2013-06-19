from django.db import models
from apps.worldmap import data_options

class PCVProfile(models.Model):
    is_pcv = models.BooleanField(default=True)
    user = models.OneToOneField('auth.User')
    country = models.CharField("Post Country", choices=data_options.COUNTRY_CHOICES, max_length=128, blank=True)
    sector = models.CharField(choices=data_options.SECTORS, max_length=128, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    home_address = models.CharField(max_length=128, blank=True, default="")
    home_state = models.CharField(choices=data_options.STATES, max_length=128, blank=True, default="")
    bio = models.TextField(blank=True)
    def __unicode__(self):
        return self.user.username

class School(models.Model):
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(choices=data_options.STATES, max_length=128, blank=True)
    school_name = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10, blank=True)
    about = models.TextField(blank=True)
    def __unicode__(self):
        return self.school_name

class Teacher(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.ForeignKey(School, blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True)
    following = models.ForeignKey('auth.User', related_name='following', blank=True, null=True)
    address = models.CharField(max_length=128, blank=True)
    bio = models.TextField(blank=True)
    def __unicode__(self):
        return self.user.username
