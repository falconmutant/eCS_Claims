from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^detalle_invoices/(?P<id>\d+)/$', 'Invoices.views.detalle'),
	url(r'^invoice/$', 'Invoices.views.invoices'),
	url(r'^historial_invoices/$', 'Invoices.views.historial')
)