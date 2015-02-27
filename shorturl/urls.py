from django.conf.urls import patterns, include, url
from django.contrib import admin

import shorturl.main.views
import shorturl.sensors.views

urlpatterns = patterns('',
    url(r'^$', shorturl.main.views.URLShortener.as_view(), name='home'),
    url(r'^sensors/$', shorturl.sensors.views.SensorData.as_view(), name='sensors'),
    url(r'^add/$', shorturl.sensors.views.SensorAdder.as_view(), name='add'),        
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<code>\w+)/$', shorturl.main.views.Redirect.as_view(), name='redirect'),              
)
