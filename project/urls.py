from django.conf.urls import patterns, include, url
from django.contrib import admin

from generator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.FrontView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
