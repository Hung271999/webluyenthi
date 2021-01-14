from django.urls import path
from django.conf.urls import url
from .import views
urlpatterns = [
     url(r'^login$', views.LoginClass.as_view(), name='login'),
     url(r'^register$',views.register.as_view(), name='register'),
     url(r'^changepassword$', views.changepassword.as_view(), name='changepassword'),
     url(r'^logout$', views.logoutt, name='logout'),
]  