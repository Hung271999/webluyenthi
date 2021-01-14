from django.urls import path
from django.conf.urls import url
from .import views
urlpatterns = [
     url(r'^detailExam/(?P<id>[0-9]+)/$', views.detailExam,name="detailExam"),
     url(r'^result//(?P<id>[0-9]+)/$',views.result,name="result"),
     url(r'^detailResult/(?P<id>[0-9]+)/$', views.detailResult,name="detailResult"),
     url(r'^detailSubjects/(?P<id>[0-9]+)/$', views.detailSubjects,name="detailSubjects"),
     url(r'^file$', views.file, name='file'),
     url(r'^tutorial$', views.tutorial, name='tutorial'),
]  
