from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'McGlennInspections.blog.views.home', name='blog'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
