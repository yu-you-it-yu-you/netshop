from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^$', views.ToOrder.as_view()),
    url(r'^order.html$', views.OrderList.as_view()),
]