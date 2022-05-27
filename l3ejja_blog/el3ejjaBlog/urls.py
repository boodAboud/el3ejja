# -*- coding: utf-8 -*-

from django.urls import path
from . import views
#from django.conf.urls import url
from django.urls import include, re_path

urlpatterns = [
    re_path('', views.index, name='index'),
    #re_path('docs/', include('docs.urls'))
]
