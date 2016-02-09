"""ecsclaims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from claims import urls as claims_urls
from app import urls as app_urls
from claims.views import routes, login
from app.views import apptoken, AppResetKeyView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('claims_Web.urls')),
    url(r'^proveedores', include('claims.urls')),
    url(r'^apps/', include("app.urls")),
    url(r'^auth/login$', login, name='login'),
    url(r'^', include('django.contrib.auth.urls')),
    #url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^routes/', routes, name='routes'),
    url(r'^', include('invoices_Web.urls')),
    url(r'^', include('settings.urls')),
    url(r'^explorer/', include('explorer.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
