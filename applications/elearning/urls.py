# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
from applications.elearning.views.views_crud import robot_files
from applications.elearning.views import views_crud as views
__author__ = 'Guinsly'

urlpatterns = [
      #url(r'^$', views.hello, name='index'),
      url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='home-files'),

      url(r'^$', views.HomeView.as_view(), name='index'),
      url(r'^dashboard/$', views.DashBoard.as_view(), name='index'),

        ]
