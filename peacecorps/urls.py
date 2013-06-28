import os

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from apps.worldmap.views import MapView


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', MapView.as_view(), name="map_view"),
    url(r'^map/', include('apps.worldmap.urls')),

    url(r'^user/', include('apps.pcvcore.urls')),

    # Examples:
    # url(r'^$', 'peacecorps.views.home', name='home'),
    # url(r'^peacecorps/', include('peacecorps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$','data.views.home',name='home'),
    # url(r'^register/$', 'data.views.register', name="register")
    url(r'^blog/', include('apps.pcvblog.urls')),
    url(r'^pcv/', include('apps.pcvblog.pcv_tools.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={'document_root': settings.MEDIA_ROOT}), )
