from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken
from Login import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'Login/$', CustonAuthToken.as_view()),
    re_path(r'example_lista2/$',views.Example2List.as_view()),
   
]