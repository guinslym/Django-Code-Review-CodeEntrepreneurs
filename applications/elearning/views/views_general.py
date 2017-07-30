from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect


#logging
import logging
logger = logging.getLogger(__name__)

#http://localhost:8001/
class DashBoard(LoginRequiredMixin, TemplateView):
    """
    Return 
    """
    template_name='elearning/dashboard.html'

    def get_context_data(self, **kwargs):
        #
        context = super(DashBoard, self).get_context_data(**kwargs)
        context['msg'] = 'hello world'

        return context

class ShowVideoTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'elearning/show_course_video.html'




def robot_files(request, filename):
    return render(request, 'elearning/'+filename, {}, content_type="text/plain")

def handler404(request):
    response = render(request, 'elearning/page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'elearning/server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response