from django.urls import path
from django.conf.urls import url
from . import views
from things.views import *

app_name = 'things'

urlpatterns = [
    path('', ThingsList.as_view(), name='index'),
    path('create/', ThingCreate.as_view(), name='device_create'),
    url('registration/', CreateAccount.as_view(), name='create_account'),
    # url('sing_in/', views.SingIn.as_view(), name='sing_in'),
    # url('sing_out/', views.SingOut.as_view(), name='sing_out'),
    url(r'^(?P<pk>[0-9]+)/$', ThingView.as_view(), name='device_details'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ThingDelete.as_view(), name='device_delete'),

]
