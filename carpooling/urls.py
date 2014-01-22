from django.conf.urls import patterns, include, url

from django.contrib import admin
from carpooling.core import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carpooling.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^carpooling/', include('carpooling.core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
