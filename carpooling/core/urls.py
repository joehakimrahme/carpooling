from django.conf.urls import patterns, url

from carpooling.core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ad_id>\d+)$', views.show, name='show'),
)
