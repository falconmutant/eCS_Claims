from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^invoices_detalle/(?P<id>\d+)/$', 'Invoices.views.detalle'),
	url(r'^invoice/$', 'Invoices.views.invoices'),
	url(r'^invoices_historial/$', 'Invoices.views.historial')
)