from django.conf.urls import patterns, include, url
#from . import views

urlpatterns = patterns('',


	url(r'^$', 'claims_Web.views.index'),
	url(r'^login/$' , 'django.contrib.auth.views.login',
		{'template_name':'login.html'}, name='login'),
	url(r'^logged_in/$', 'claims_Web.views.logged_in'),
	url(r'^detalles/(?P<id>\d+)/$', 'claims_Web.views.detalle'),
	url(r'^historial_detalles/(?P<id>\d+)/$', 'claims_Web.views.detalle_historial'),
	url(r'^claims/$', 'claims_Web.views.claims'),
	url(r'^historial/$', 'claims_Web.views.historial'),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout',
						{'next_page': 'claims_Web.views.index'}),
	url(r'permisos/$', 'claims_Web.views.permisos'),
	url(r'^permission/$', 'claims_Web.views.save_permission'),
	url(r'^registro/$', 'claims_Web.views.registration'),
	#url(r'^motivosLista/$', 'claims_Web.views.MotivosLista.as_view()', name='mLista'),
)
