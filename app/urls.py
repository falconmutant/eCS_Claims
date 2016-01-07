from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^token$', apptoken, name='apptoken'),
    url(r'^validate', validate_token , name='validate_token'),
    url(r'^(?P<app_id>\d+)/$', AppHomeView.as_view(), name='apphome'),
    url(r'^(?P<app_id>\d+)/admins$', AppHomeView.as_view(), name='appadmins'),
    url(r'^(?P<app_id>\d+)/key$', AppResetKeyView.as_view(), name='resetkey'),
    url(r'^$', select_app, name='select'),
)
