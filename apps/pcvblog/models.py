from django.db import models

class Entry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog-images")
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

