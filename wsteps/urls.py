from django.conf.urls import patterns, url
import views

urlpatterns = patterns('wsteps.views',
                       url(r'^$', views.index),
                       url(r'^submit', views.submit, name='submit_step_view'),
                       url(r'^help', views.help, name='help_view'),
                       )
