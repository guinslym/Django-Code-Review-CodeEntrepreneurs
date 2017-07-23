# -*- coding: utf-8 -*
from django.conf.urls import url, include

from django.views import generic
from django.views.decorators.cache import cache_page
from applications.elearning.views.views_crud import robot_files
from applications.elearning.views import views_crud
__author__ = 'Guinsly Mondesir'

urlpatterns = [
      #url(r'^$', views.hello, name='index'),
      url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='home-files'),

      url(r'^$', views_crud.HomeView.as_view(), name='index'),

      ]
