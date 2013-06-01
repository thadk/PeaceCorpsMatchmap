from django.db import models

class Entry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    image = models.ImageField()
    body = models.TextField()

