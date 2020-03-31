from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Profile import views
from Profile.views import CustonAuthToken

urlpatterns = [

    re_path(r'PerfilList/$',views.PerfilList.as_view()),
    re_path(r'EstadoList/$',views.EstadoList.as_view()),
    re_path(r'GeneroList/$',views.GeneroList.as_view()),
    re_path(r'CiudadList/$',views.CiudadList.as_view()),
    re_path(r'EstadoCivilList/$',views.EstadoCivilList.as_view()),
    re_path(r'OcupacionList/$',views.OcupacionList.as_view()),
]
