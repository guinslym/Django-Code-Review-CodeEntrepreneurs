# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()
from django.views.decorators.cache import cache_page
from django.conf.urls.i18n import i18n_patterns
from applications.elearning.views.views_crud import robot_files

urlpatterns = [
	url(r'^(?P<filename>(robots.txt)|(humans.txt))$', robot_files, name='home-files'),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^ilovemyself/', include(admin.site.urls)),
]

#handler404 = 'applications.elearning.views.views_crude.handler404'
#handler500 = 'applications.elearning.views.views_crude.handler500'