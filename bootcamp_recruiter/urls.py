from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^companys/(?P<name>.*)/$', views.company_detail, name='company_detail'),
    url(r'^twitter/(?P<company_name>.*)$', views.query, name='query'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^query$', views.query, name='query'),
    url(r'^tweet', views.tweet, name='tweet'),
]
