from django.urls import path
from django.conf.urls import url
from . import views
from things.views import ThingsList, ThingsId

app_name = 'things'

urlpatterns = [
    path('', ThingsList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', ThingsId.as_view(), name='device_details'),


]
