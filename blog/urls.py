from django.conf.urls import patterns, include, url

from . import views


prefix = "blog_"

urlpatterns = patterns('',
    url(r'^create/$', views.BlogPostCreateView.as_view(), name=prefix + "create"),
    url(r'^(?P<slug>\S+)/update/$', views.BlogPostUpdateView.as_view(), 
        name=prefix + "update"),
    url(r'^$', views.BlogHomeTemplateView.as_view(), name=prefix + "home"),
    url(r'^(?P<slug>\S+)/$', views.BlogPostDetailView.as_view(), 
        name=prefix + "post"),
)
