from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^steps/', include('wsteps.urls')),
                       url(r'^$', views.index),
                       )

# Serve static files for admin, use this for debug usage only
# `python manage.py collectstatic` is preferred.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
