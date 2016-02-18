from django.conf.urls import patterns, include, url
#from . import views

urlpatterns = patterns('',

	url(r'^$', 'settings.views.index'),
	url(r'^login/$' , 'django.contrib.auth.views.login',
		{'template_name':'login.html'}, name='login'),
	url(r'^logged_in/$', 'settings.views.logged_in'),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout',
						{'next_page': 'settings.views.index'}),
	url(r'permisos/$', 'settings.views.permisos'),
	url(r'^permission/$', 'settings.views.save_permission'),
	url(r'^registro/$', 'settings.views.registration'),
	url(r'^localidades/$', 'settings.views.localitys'),
	url(r'^motivos/$', 'settings.views.reasons'),
	url(r'^logic/$', 'settings.views.erace'),
	
)
