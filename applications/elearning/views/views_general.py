from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

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

def robot_files(request, filename):
    return render(request, 'elearning/'+filename, {}, content_type="text/plain")
