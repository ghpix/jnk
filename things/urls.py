from django.urls import path
from django.conf.urls import url
from . import views
from things.views import *

app_name = 'things'

urlpatterns = [
    path('', ThingsList.as_view(), name='index'),
    path('create/', ThingCreate.as_view(), name='device_create'),
    url(r'^(?P<pk>[0-9]+)/$', ThingView.as_view(), name='device_details'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ThingDelete.as_view(), name='device_delete'),

]
