from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomeTemplateView.as_view(), name="home"),
)
