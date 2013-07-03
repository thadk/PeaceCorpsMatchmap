from django.conf.urls import patterns, url
from .views import EntryCreate, EntryList, EntryUpdate

# pcv views
urlpatterns = patterns('',
    url(r'^$', EntryList.as_view(), name='entry_list'),
    url(r'^entry/create/$', EntryCreate.as_view(), name='entry_create'),
    url(r'^entry/(?P<pk>\d+)/$', EntryUpdate.as_view(), name='entry_update'),
    url(r'^entry/(?P<entry_pk>\d+)/delete/$', 'apps.pcvblog.pcv_tools.views.entry_delete', name='entry_delete'),
)