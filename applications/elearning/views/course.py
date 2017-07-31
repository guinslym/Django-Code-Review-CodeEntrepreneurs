    # -*- coding: utf-8 -*-

# Standard Python module
from json import dumps, loads
from datetime import datetime, timedelta, time
import os

#Django
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
#https://docs.djangoproject.com/fr/1.11/ref/class-based-views/
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

#Protection
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#pagination
from django.core.paginator import (
	Paginator, 
	EmptyPage, 
	PageNotAnInteger
	)
#Task queues
#cache
from django.views.decorators.cache import cache_page

#logging
import logging
logger = logging.getLogger(__name__)
#models
from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from django.contrib.auth.models import User

from applications.elearning.forms import CourseForm
from braces.views import PrefetchRelatedMixin
from braces.views import SelectRelatedMixin
from hitcount.views import HitCountDetailView

#http://localhost:8001/
class CourseListView(LoginRequiredMixin, ListView):

    model = Course
    paginate_by = 9
    template_name = 'elearning/homepage.html'
    #not sure about this next line
    prefetch_related = ['course_set__user', 'user_set_userprofile']

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#http://localhost:8001/
class CourseDetailView(LoginRequiredMixin, HitCountDetailView, DetailView):
    model = Course
    template_name = 'elearning/course_detail.html'
    prefetch_related = ['course_set__user']
    count_hit = True    # set to True if you want it to try and count the hit

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

product_detail = CourseDetailView.as_view()

#http://localhost:8001/
class AdminCourseListView(LoginRequiredMixin, ListView):

    model = Course
    paginate_by = 6
    template_name = 'elearning/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CourseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "elearning/course_update.html"
    success_message = 'Successfully Updated a Course entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

    def get_success_url(self):
            if 'slug' in self.kwargs:
                slug = self.kwargs['slug']
            else:
                slug = 'demo'
            return reverse('elearning:course_detail', kwargs={'slug': slug})

product_update = login_required(CourseUpdateView.as_view())

class CourseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CourseForm
    template_name = "elearning/course_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super(CourseCreateView, self).form_valid(form)

product_new = login_required(CourseCreateView.as_view())


class  CourseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Course
    success_message = "Session %(name)s was removed successfully"
    success_url = reverse_lazy('elearning:courses_home')
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user == self.object.author:
            # Return the appropriate response
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message % obj.__dict__)
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponse('not the owner')

product_update = login_required(CourseUpdateView.as_view())

