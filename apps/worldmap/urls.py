from django.conf.urls import patterns, include, url

from .views import BlogJSON

urlpatterns = patterns('',

    # url(r'^$', MapView.as_view(), name="map_view"),
    url(r'get_blogs/$', BlogJSON.as_view(), name="blog_json"),

)
