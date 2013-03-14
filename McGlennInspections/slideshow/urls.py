from django.conf.urls import patterns, url
from slideshow import views


urlpatterns = patterns('',
    url(r'^$', views.slideshow_page, name='slideshow'),
    url(r'^details', views.slideshow_detail_page, name='slideshow_details'),
)
