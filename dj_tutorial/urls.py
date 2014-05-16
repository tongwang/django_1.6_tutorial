from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('dj_tutorial.apps.polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
