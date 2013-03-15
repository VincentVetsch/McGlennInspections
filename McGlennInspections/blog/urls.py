from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
    url(r'^$', views.blog_page),
    url(r'^details', views.blog_page_details, name='details'),
)
