from django.conf.urls import url
from django.contrib.auth import views


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name="add"),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout'),
]
