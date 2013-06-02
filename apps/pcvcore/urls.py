from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="base.html")),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name':"user/login.html"}, name="login"
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="logout"
    ),
)
