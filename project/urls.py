from django.conf.urls import patterns, include, url
from django.contrib import admin

from generator import views


urlpatterns = patterns('',

    url(r'^$', views.FrontView.as_view()),
    url(r'^api/generate-ipsum/$', views.GenerateIpsumView.as_view()),

    url(r'^admin/', include(admin.site.urls)),

)
