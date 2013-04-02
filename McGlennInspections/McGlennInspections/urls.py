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
    url(r'^$', 'pages.views.mcglenn'),
    url(r'^sop/', 'pages.views.sop'),
    url(r'^ethics/', 'pages.views.ethics'),
    url(r'^agreement/', 'pages.views.agreement'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^glossary/', include('glossary.urls')),
    url(r'^slideshow/', include('slideshow.urls')),
    url(r'^rvalues/', include('rvalues.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^cust_feedback/', include('cust_feedback.urls')),
)
urlpatterns += staticfiles_urlpatterns()
