from django.conf.urls import patterns, url

from .views import BlogJSON, Entries, Permalink

urlpatterns = patterns('',

    # utility views
    url(r'^entries.json/$', BlogJSON.as_view(), name='new_blog_json'),
    url(r'^tags/$', TagJSON.as_view(), name='tag_json'),

    # public views
    url(r'^$', Entries.as_view(), name="blog_entries"),
    url(r'^entry/(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/$', Permalink.as_view(), name="blog_permalink"),
    url(r'^(?P<pcv>[\w-]+)/$', Entries.as_view(), name="blog_user_entries"),
)
