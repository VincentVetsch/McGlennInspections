from django.conf.urls import patterns, url
from appointment import views


urlpatterns = patterns('',
    url(r'^$', views.appointment, name='appointment'),
    url(r'^add_inspector/$', views.appointment_add_inspector, name='add_inspector'),
    url(r'^change_status/$', views.appointment_change_status, name='change_status'),
    url(r'^(?P<appointment_slug>.*)/$', views.appointment_details, name='appointment_details'),
    url(r'^appointment_form/$', views.appointment_form, name='appointment_form'),
)
