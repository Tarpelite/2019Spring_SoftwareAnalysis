from django.urls import path,include
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'login/', views.login),
    url(r'register', views.register),
    url(r'index/', views.index),
]
