from django.urls import path
from . import views

app_name = 'things'

urlpatterns = [
    path('', views.things_index, name='index'),
    # path('$Index_Name_2/', views.$Index_Name_2, name='$Some_Link_Name'),
]
