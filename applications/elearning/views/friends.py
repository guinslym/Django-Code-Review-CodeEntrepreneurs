# -*- coding: utf-8 -*-

# Standard Python module
from json import dumps, loads
from datetime import datetime, timedelta, time
import os

#Django
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
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
from django.contrib.auth.models import User
from friendship.models import Friend, Follow

from applications.elearning.forms import CourseForm


#http://localhost:8001/

"""
Create a view to see a list of Friends
.. using django-friendship
"""

class friendsView(TemplateView):
	template_name = 'friends/inbox.html'