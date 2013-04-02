from django.conf.urls import patterns, url
from appointment import views


urlpatterns = patterns('',
    url(r'^$', views.appointment, name='appointment'),
    url(r'^completed/$', views.appointment_completed, name='appointment_completed'),
    url(r'^completed/(?P<appointment_slug>.*)/$', views.appointment_details, name='appointment_details'),
    url(r'^change_status/$', views.appointment_change_status, name='change_status'),
    url(r'^inspector/(?P<appointment_slug>.*)/$', views.change_inspector, name='change_inspector'),
    url(r'^inspector_notes/(?P<appointment_slug>.*)/$', views.inspector_notes, name='inspector_notes'),
    url(r'^(?P<appointment_slug>.*)/$', views.appointment_details, name='appointment_details'),
    url(r'^appointment_form/$', views.appointment_form, name='appointment_form'),
)
