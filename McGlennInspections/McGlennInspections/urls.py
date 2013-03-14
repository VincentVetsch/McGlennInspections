'''
    Django settings for McGlennInspections project.

    For more information on this file, see
    https://docs.djangoproject.com/en/dev/ref/urls/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^glossary/', include('glossary.urls')),
    url(r'^slideshow/', include('slideshow.urls')),
    url(r'^rvalues/', include('rvalues.urls')),
    url(r'^cust_feedback/', include('cust_feedback.urls')),
)
