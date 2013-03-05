from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# TODO -- setup urls for McGlennInspections

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'McGlennInspections.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
