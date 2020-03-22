from django.conf.urls import url

from goods import views
from netshop.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^category/(\d+)$', views.IndexView.as_view()),
    url(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    url(r'goodsdetails/(\d+)', views.DetailView.as_view())
]