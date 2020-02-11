from django.urls import path
from django.conf.urls import url
from . import views
from things.views import *

app_name = 'things'

urlpatterns = [
    # path('', views.things_index, name='index'),
    path('', ThingsList.as_view(), name='index'),
    # path('<int:device_id>', views.things_id, name='index_id'),
    path('<int:device_id>', ThingsId.as_view(), name='device_details'),
    # url(r'^(?P<pk>\d+)$', ThingsId.as_view(), name='device_details'),

]
