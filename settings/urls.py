from django.conf.urls import patterns, include, url
#from . import views

urlpatterns = patterns('',


	url(r'^registro/$', 'settings.views.registration'),
	url(r'^localidades/$', 'settings.views.localitys'),
	url(r'^motivos/$', 'settings.views.reasons'),
)
