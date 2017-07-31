# -*- coding: utf-8 -*-

WSGI_APPLICATION = 'main.wsgi.application'
ROOT_URLCONF = 'main.urls'
SITE_ID=1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os
import re
import json

logging.log(logging.INFO, 'loading settings for ' + __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


BASE_APPS =  (
    #Third party app but I need to place it here (above django..)
    'flat_responsive',
    
    #django based
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',

    #django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
)

THIRD_PARTY_APPS =  (
    #django-crispy-forms
    'crispy_forms',
    #django-bootstrap-pagination
    'bootstrap_pagination',
    #django-vote
    'vote',
    #django-friendship
    "friendship",
    #django rest framework (DRF)
    'rest_framework',
    #django-admin-honeypot
    'admin_honeypot',
    #django-hitcount
    'hitcount',
)

LOCAL_APPS = (
    "applications.elearning",
)

'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
'''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                #'django_messages.context_processors.inbox',
            ],
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

USE_TZ = True

gettext = lambda x: x

LANGUAGES = (
   ('fr', gettext('French')),
   ('en', gettext('English')),
)

DEFAULT_LANGUAGE = 0

LOCALE_PATHS = ('locale', )

GOOGLE_ANALYTICS_PROPERTY_ID = ''
GOOGLE_ANALYTICS_SITE_SPEED = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ckeditor settings
CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = \
    '//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [{
            'name': 'basic',
            'items': ['Bold', 'Italic', 'Underline', 'RemoveFormat', '-',
                      'PasteText', 'Undo', 'Redo', 'Format', 'Source', ],
        }],
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


LOGIN_REDIRECT_URL = "/"
SHELL_PLUS = "ipython"

LOGOUT_URL='/'
