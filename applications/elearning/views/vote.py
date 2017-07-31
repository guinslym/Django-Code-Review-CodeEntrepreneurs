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
from django.conf import settings
from django.http import HttpResponseRedirect

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

class VoteUpOrDownView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=kwargs['slug'] )
        user_id = request.user.id
        #import ipdb; ipdb.set_trace()
        if course in Course.votes.all(user_id):
            course.votes.delete(user_id)
            messages.success(request, 'We deleted your Like')
            return redirect(reverse('elearning:course_detail',kwargs={'slug':kwargs['slug']}))
        else:
            course.votes.up(user_id)
            messages.success(request, 'Thanks for liking my Course')
            return redirect(reverse('elearning:course_detail',kwargs={'slug':kwargs['slug']}))
