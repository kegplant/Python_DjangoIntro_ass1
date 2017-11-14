from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'create$',views.create),
    url(r'new$',views.new),
    url(r'create$',views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$',views.edit),
    url(r'^(?P<number>\d+)/delete$',views.destroy),
]