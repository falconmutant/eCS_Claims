from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'index.html'}, name='login'),
	url(r'^logged_in/$', 'Claims.views.logged_in'),
	url(r'^detalles/$', 'Claims.views.detalle'),
	url(r'^claims/$', 'Claims.views.claims'),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout')
)