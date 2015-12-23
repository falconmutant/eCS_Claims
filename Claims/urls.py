from django.conf.urls import patterns, include, url

urlpatterns = patterns('',


	url(r'^$', 'Claims.views.index'),
	url(r'^login/$' , 'django.contrib.auth.views.login',
		{'template_name':'login.html'}, name='login'),
	url(r'^logged_in/$', 'Claims.views.logged_in'),
	url(r'^detalles/(?P<id>\d+)/$', 'Claims.views.detalle'),
	url(r'^claims/$', 'Claims.views.claims'),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout',
						{'next_page': 'Claims.views.index'})
)