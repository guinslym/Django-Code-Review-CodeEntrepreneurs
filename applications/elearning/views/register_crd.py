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
from django.contrib.auth.models import User

from applications.elearning.forms import CourseForm

#http://localhost:8001/
class RegisterListView(LoginRequiredMixin, ListView):

    model = Register
    template_name = 'course_registration/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RegisterAndUnRegister(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        course = get_object_or_404( Course, pk=int(kwargs['pk']) )
        user_is_registered = Register.objects.filter(course=course, student=request.user)
        import pdb; pdb.set_trace()
        if not user_is_registered:
            Register.objects.create(
            course= course,
            student= request.user
            )
            messages.success("Congrats!!! Registered to this course")
            return redirect(reverse('elearning:course_detail',kwargs={'pk':int(kwargs['pk'])}))
        else:
            user_is_registered.delete()
            messages.error("You are Unregistered to this course")
            return redirect(reverse('elearning:course_detail',kwargs={'pk':int(kwargs['pk'])}))

