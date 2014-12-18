from django.conf.urls import patterns, include, url

from . import views


prefix = "blog_"

urlpatterns = patterns('',
    url(r'search/$', views.BlogSearchListView.as_view(), name=prefix + "search"),
    url(r'create/$', views.BlogPostCreateView.as_view(), name=prefix + "create"),
    url(r'(?P<slug>\S+)/update/$', views.BlogPostUpdateView.as_view(), 
        name=prefix + "update"),
    url(r'(?P<slug>\S+)/$', views.BlogPostDetailView.as_view(), 
        name=prefix + "post"),
    url(r'$', views.BlogHomeTemplateView.as_view(), name=prefix + "home"),

)
