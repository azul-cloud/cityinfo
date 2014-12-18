from django.conf.urls import patterns, include, url

from . import views


prefix = "region_"

urlpatterns = patterns('',
    url(r'city/(?P<slug>\S+)/$', views.CityListView.as_view(), 
        name=prefix + "city"),
    url(r'country/(?P<slug>\S+)/$', views.CountryListView.as_view(), 
        name=prefix + "country"),
)
