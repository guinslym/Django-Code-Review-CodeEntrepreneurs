# -*- coding: utf-8 -*-

# Standard Python module
from json import dumps, loads
from datetime import datetime, timedelta, time

import os

#Django
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

#pagination
from django.core.paginator import (
	Paginator, 
	EmptyPage, 
	PageNotAnInteger)
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

#http://localhost:8001/
class HomeView(generic.TemplateView):
    """
    Return 
    """
    template_name='elearning/home.html'

    def get_context_data(self, **kwargs):
        """
        Return ....
        """
        #
        context = super(HomeView, self).get_context_data(**kwargs)
        context['msg'] = 'hello world'

        return context