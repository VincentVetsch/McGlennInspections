from django.conf.urls import patterns, url
from glossary import views


urlpatterns = patterns('',
    url(r'^$', views.glossary_page, name='glossary'),
    url(r'^details', views.glossary_page_details, name='glossary_details'),
)
