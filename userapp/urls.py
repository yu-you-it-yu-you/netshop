from django.conf.urls import url
from django.urls import path, include

from userapp import views

urlpatterns = {
    url(r'^register/', views.Register.as_view()),
    url(r'^checkUname/', views.CheckUname.as_view()),
    url(r'^center/', views.Center.as_view()),
    url(r'^logout/', views.Logout.as_view()),
    url(r'^login/', views.Login.as_view()),
    url(r'^loadCode.jpg', views.LoadCode.as_view()),
    url(r'^checkcode/', views.Checkcode.as_view()),
    url(r'^address/', views.Addressa.as_view()),
    #url(r'^loadArea', views.LoadArea.as_view()),

}


