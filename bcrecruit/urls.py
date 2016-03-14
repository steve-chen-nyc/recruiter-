"""bcrecruit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from bootcamp_recruiter import views
from rest_framework import routers

router = routers.DefaultRouter();
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('bootcamp_recruiter.urls')),
    url(r'^', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_frameworks')),
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]
