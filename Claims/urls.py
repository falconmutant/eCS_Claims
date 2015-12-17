from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'index.html'}, name='login'),
	url(r'^logged_in/$', 'app.views.logged_in'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout')
)