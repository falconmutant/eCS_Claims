from django.conf.urls import patterns, include, url
from claims_Web import views

urlpatterns = patterns('',

	url(r'^$', views.index.as_view(),name="index"),
	url(r'^login/$' , 'django.contrib.auth.views.login',
		{'template_name':'login.html'}, name='login'),
	url(r'^logged_in/$', views.logged_in.as_view(),name="logged_in"),
	url(r'^detalles/(?P<id>\d+)/$', views.detalle.as_view(),name="detalles"),
	url(r'^historial_detalles/(?P<id>\d+)/$', views.detalle_historial,name="historial_detalles"),
	url(r'^claims/$', views.claims.as_view(),name="claims"),
	url(r'^historial/$', views.historial.as_view(),name="historial"),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout',
						{'next_page': 'claims_Web.views.index'}),
	url(r'permisos/$', views.permisos.as_view(),name="permisos"),
)
