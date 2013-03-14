from django.conf.urls import patterns, url
from cust_feedback import views


urlpatterns = patterns('',
    url(r'^$', views.cust_feedback_page, name='cust_feedback'),
    url(r'^details', views.cust_feedback_page_details, name='cust_feedback_details'),
)
