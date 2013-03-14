from django.conf.urls import patterns, url
from rvalues import views


urlpatterns = patterns('',
    url(r'^$', views.rvalues_page, name='rvalues'),
    url(r'^details', views.rvalues_page_details, name='rvalues_details'),
)
