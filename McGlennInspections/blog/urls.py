from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
    url(r'^$', views.blog_page, name='blog'),
    url(r'^details', views.blog_details, name='details'),
)
