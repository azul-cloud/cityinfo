from django.conf.urls import patterns, include, url

from blog import views


prefix = "blog-"

urlpatterns = patterns('',
    url(r'^$', views.BlogHomeTemplateView.as_view(), name=prefix + "home"),
    url(r'^(?P<slug>\S+)/$', views.BlogPostDetailView.as_view(), 
    	name=prefix + "post"),
)
