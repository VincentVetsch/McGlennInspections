from django.conf.urls import patterns, url
from rvalues import views


urlpatterns = patterns('',
    url(r'^$', views.rvalues_page, name='rvalues'),
    url(r'^details', views.rvalues_detials_page, name='rvalues_details'),
)
