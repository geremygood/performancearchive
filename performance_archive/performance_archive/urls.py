from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^performance/$', 'archive.views.index'),
    url(r'^performance/(?P<archive_performance_id>\d+)/$', 'archive.views.detail'),
    url(r'^performance/(?P<archive_performance_id>\d+)/results/$', 'archive.views.results'),
#    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
