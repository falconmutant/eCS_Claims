from django.conf.urls import patterns, url
from claims.views import *

urlpatterns = patterns('',
    url(r'^/(?P<rfc>\w+)/eventos$', views.EventosView.as_view(), name='eventos'),
    url(r'^/(?P<rfc>\w+)/eventos/$', views.EventosView.as_view(), name='eventos'),
    url(r'^/(?P<rfc>\w+)$', views.ProveedoresView.as_view(), name='proveedor'),
    url(r'^/(?P<rfc>\w+)/$', views.ProveedoresView.as_view(), name='proveedor'),
    url(r'^/(?P<rfc>\w+)/eventos/(?P<evento_id>\d+)$', views.EventoDetailView.as_view(), name='evento')
)
