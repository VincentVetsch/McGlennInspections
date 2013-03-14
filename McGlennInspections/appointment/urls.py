from django.conf.urls import patterns, url
from appointment import views


urlpatterns = patterns('',
    url(r'^$', views.appointment_page, name='appointment'),
    url(r'^details', views.appointment_page_details, name='appointment_details'),
)
