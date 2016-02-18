from django.conf.urls import patterns, include, url
#from . import views

urlpatterns = patterns('',

	url(r'^detalles/(?P<id>\d+)/$', 'claims_Web.views.detalle'),
	url(r'^historial_detalles/(?P<id>\d+)/$', 'claims_Web.views.detalle_historial'),
	url(r'^claims/$', 'claims_Web.views.claims'),
	url(r'^historial/$', 'claims_Web.views.historial'),
)
