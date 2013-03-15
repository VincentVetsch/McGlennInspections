'''
    Django settings for McGlennInspections project.

    For more information on this file, see
    https://docs.djangoproject.com/en/dev/ref/urls/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin
from McGlennInspections import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('blog.urls')),
    (r'^appointment/', include('appointment.urls')),
    (r'^glossary/', include('glossary.urls')),
    (r'^slideshow/', include('slideshow.urls')),
    (r'^rvalues/', include('rvalues.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^cust_feedback/', include('cust_feedback.urls')),
)
urlpatterns += staticfiles_urlpatterns()
