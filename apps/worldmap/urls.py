from django.conf.urls import patterns, include, url

from .views import BlogJSON, DataOptionsJSON

urlpatterns = patterns('',

    # url(r'^$', MapView.as_view(), name="map_view"),
    url(r'get_blogs/$', BlogJSON.as_view(), name="blog_json"),
    url(r'get_data_options/$', DataOptionsJSON.as_view(), name="data_options_json"),

)