from django.conf.urls import patterns, url
from blog import views

# DONE - Add Comments url
urlpatterns = patterns('',
    url(r'^$', views.blog_page),
    url(r'^details', views.blog_page_details, name='details'),
    url(r'^comments', views.blog_comments),
)
