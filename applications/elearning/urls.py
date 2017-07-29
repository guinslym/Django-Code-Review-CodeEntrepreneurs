# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
from applications.elearning.views import course_crud as views
from applications.elearning.views import profile_rud as userprofile
from applications.elearning.views import views_general as gviews
__author__ = 'Guinsly'


urlpatterns = [
   #courses
   url(r'^course_create/$', views.CourseCreateView.as_view(), name='course_create'),
   url(r'^course_update/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='course_update'),
   url(r'^course_detail/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course_detail'),
   url(r'^course_delete/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course_delete'),
   url(r'^$', views.CourseListView.as_view(), name='courses_home'),
   url(r'^$', views.CourseListView.as_view(), name='index'),

   #userprofile
   url(r'^userprofile_list/$', userprofile.UserProfileListView.as_view(), name='userprofile_list'),
   url(r'^userprofile_update/(?P<pk>\d+)/$', userprofile.UserProfileUpdateView.as_view(), name='userprofile_update'),
   url(r'^userprofile_detail/(?P<pk>\d+)/$', userprofile.UserProfileDetailView.as_view(), name='userprofile_detail'),
   url(r'^userprofile_delete/(?P<pk>\d+)/$', userprofile.UserProfileDeleteView.as_view(), name='userprofile_delete'),

      #url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),

      # url(r'^$', views.HomeView.as_view(), name='index'),
      url(r'^dashboard/$', gviews.DashBoard.as_view(), name='index'),

        ]


