from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db import models

from taggit.managers import TaggableManager

class Entry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog-images", null=True, blank=True)
    slug = models.SlugField(db_index=True, blank=True)
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    @property
    def abstract(self):
        return self.body[:30] + "..."

    def save(self, *args, **kwargs):
        ## TODO: Should slug be unique? If so we need db constraint
        #        and a check here or in ``clean``
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('entry_list')

    def __unicode__(self):
        return "%s - %s" % (self.title, self.author)
