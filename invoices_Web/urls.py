from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^detalle_invoices/(?P<id>\d+)/$', 'invoices_Web.views.detalle'),
	url(r'^invoice/$', 'invoices_Web.views.invoices'),
	url(r'^historial_invoices/$', 'invoices_Web.views.historial')
	url(r'^save_ligar/$', 'invoices_Web.views.save_ligar')
)