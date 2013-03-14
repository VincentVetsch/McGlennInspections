from django.conf.urls import patterns, url
from glossary import views


urlpatterns = patterns('',
    url(r'^$', views.glossary_page, name='glossary'),
    url(r'^details', views.glossary_details_page, name='glossary_details'),
)
