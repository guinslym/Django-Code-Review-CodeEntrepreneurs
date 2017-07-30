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
from applications.elearning.models import UserProfile
from applications.elearning.models import UserProfile
from django.contrib.auth.models import User

from applications.elearning.forms import UserProfileForm

#http://localhost:8001/
class UserProfileListView(LoginRequiredMixin, ListView):

    model = UserProfile
    paginate_by = 5
    template_name = 'userprofile/userprofile_homepage.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#http://localhost:8001/
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'userprofile/userprofile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

product_detail = UserProfileDetailView.as_view()

class UserProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile/userprofile_update.html"
    success_message = 'Successfully Updated a UserProfile entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

product_update = login_required(UserProfileUpdateView.as_view())

class  UserProfileDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UserProfile
    success_message = "Session %(name)s was removed successfully"
    success_url = reverse_lazy('elearning:userprofile_list')
    
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

product_update = login_required(UserProfileUpdateView.as_view())


"""
class UserProfileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = UserProfileForm
    template_name = "userprofile/userprofile_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super(UserProfileCreateView, self).form_valid(form)

product_new = login_required(UserProfileCreateView.as_view())
"""
