from django.conf.urls import patterns, url

from .views import BlogJSON, Entries, Permalink, TagJSON

# prefixed by /blog/
urlpatterns = patterns('',

    # utility views
    url(r'^json/$', BlogJSON.as_view(), name='blog_json'),
    url(r'^tags/$', TagJSON.as_view(), name='tag_json'),

    # public views
    url(r'^$', Entries.as_view(), name="blog_entries"),
    url(r'^(?P<pcv>[\w-]+)/$', Entries.as_view(), name="blog_user_entries"),
    url(r'^(?P<pcv>[\w-]+)/(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/$', Permalink.as_view(), name="blog_permalink"),
)
