# -*- coding: utf-8 -*-

# Standard Python module

#django
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
                                        CreateView,
                                        UpdateView,
                                        DeleteView,
                                        FormView,) 
from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

from applications.elearning.models import BankAccount, UserProfile
from django.core.urlresolvers import reverse, reverse_lazy

#create fake userProfile
from mixer.backend.django import mixer

#logging (python std)
import logging
logger = logging.getLogger(__name__)

#http://localhost:8001/
class DashBoard(LoginRequiredMixin, TemplateView):
    """
    Return 
    """
    template_name='userprofile/dashboard.html'

    def get_context_data(self, **kwargs):
        #
        context = super(DashBoard, self).get_context_data(**kwargs)
        context['msg'] = 'hello world'
        user = self.request.user
        #Create a fake UserProfile Account in case that this user just SignUp
        try:
            context['balance']= BankAccount.objects.filter(user=user).get().balance
        except:
            BankAccount.objects.create(user=user, balance=6)
            mixer.blend(UserProfile, user=user)

        context['balance']= BankAccount.objects.filter(user=user).get().balance

        return context

class ShowVideoTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'elearning/show_course_video.html'


class AddMoneyIntoAccount(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        bank = BankAccount.objects.filter(user=user).get()
        #import ipdb; ipdb.set_trace()
        to_add = 12 - bank.balance
        #add the diff
        if int(bank.balance) < 12:
            bank.balance = bank.balance + to_add
            bank.save()
            #messages('you rich')
        return redirect(reverse('elearning:dashboard'))


def robot_files(request, filename):
    return render(request, 'robots_and_errors/'+filename, {}, content_type="text/plain")

def handler404(request):
    response = render(request, 'robots_and_errors/page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'robots_and_errors/server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response