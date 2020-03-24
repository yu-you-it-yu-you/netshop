#coding=utf-8

from django.conf.urls import url

from cart import views

urlpatterns=[
    url(r'^$', views.AddCart.as_view()),
    url(r'^queryAll/$', views.CartList.as_view()),
]