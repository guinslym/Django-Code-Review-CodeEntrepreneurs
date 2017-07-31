# -*- coding: utf-8 -*
from django.conf.urls import url, include

from . import views
from django.views import generic
from django.views.decorators.cache import cache_page
from applications.elearning.views import course as views
from applications.elearning.views import profile as userprofile
from applications.elearning.views import register as register
from applications.elearning.views import vote 
from applications.elearning.views import general as gviews
__author__ = 'Guinsly'


urlpatterns = [
   #courses
   url(r'^course_create/$', views.CourseCreateView.as_view(), name='course_create'),
   url(r'^course_update/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='course_update'),
   url(r'^course_detail/(?P<slug>[-\w]{1,255})/$', views.CourseDetailView.as_view(), name='course_detail'),
   url(r'^course_delete/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course_delete'),
   url(r'^$', views.CourseListView.as_view(), name='courses_home'),

   #Register
   url(r'^register_list/$', register.RegisterListView.as_view(), name='register_list'),
   url(r'^RegisterAndUnRegister/(?P<slug>[-\w]{1,255})/$', register.RegisterAndUnRegister.as_view(), name='register_and_unregister_create'),
   #voteUpOrDown
   url(r'^voteUpOrDown/(?P<slug>[-\w]{1,255})/$', vote.VoteUpOrDownView.as_view(), name='voteUpOrDown'),
   #userprofile
   url(r'^userprofile_list/$', userprofile.UserProfileListView.as_view(), name='userprofile_list'),
   url(r'^userprofile_update/(?P<pk>\d+)/$', userprofile.UserProfileUpdateView.as_view(), name='userprofile_update'),
   url(r'^userprofile_detail/(?P<slug>[-\w]{1,255})/$', userprofile.UserProfileDetailView.as_view(), name='userprofile_detail'),
   url(r'^userprofile_delete/(?P<pk>\d+)/$', userprofile.UserProfileDeleteView.as_view(), name='userprofile_delete'),


   url(r'^show_video/(?P<slug>[-\w]{1,255})/$', gviews.ShowVideoTemplateView.as_view(), name='show_video'),
      #url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name='course-detail'),

      # url(r'^$', views.HomeView.as_view(), name='index'),
      url(r'^dashboard/$', gviews.DashBoard.as_view(), name='dashboard'),
      url(r'^AddMoneyIntoAccount/$', gviews.AddMoneyIntoAccount.as_view(), name='add_money'),

        ]


