from django.conf.urls import patterns, include, url
from django.contrib import admin

import shorturl.main.views

urlpatterns = patterns('',
    url(r'^$', shorturl.main.views.URLShortener.as_view(), name='home'),
    url(r'^(?P<code>\w+)/$', shorturl.main.views.Redirect.as_view(), name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
)
