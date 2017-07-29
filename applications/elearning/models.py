# -*- coding: utf-8 -*-

#Python standard library
import datetime
import json
import uuid

#Django package
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

#other package
from vote.models import VoteModel

from utils.models_utils import TimeStampedModel

class Course(TimeStampedModel, VoteModel, models.Model):
    author              = models.ForeignKey(User, null=False, blank=False)
    picture             = models.ImageField(upload_to='elearning/%Y/%m/%d',
                            help_text='Image of the course',
                            null=False, blank=False, verbose_name="pics")
    shortdesc           = models.CharField(
                            max_length=440,  
                            help_text='short description of the course', 
                            blank=False, verbose_name='description')
    title               = models.CharField(
                            max_length=15, 
                            help_text='title of the course', 
                            blank=False, verbose_name='title')
    slug                = models.CharField(
                            max_length=220)
    price               = models.DecimalField(
                            max_digits=16, decimal_places=2, default=5)
    number_of_minutes   = models.PositiveIntegerField(
                            validators=[
                            MinValueValidator(12),
                            MaxValueValidator(60)
                            ]
        )

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('elearning:course_detail', args=(self.id,))

    def get_authors(self):
        if self.authors:
            return '%s' % " / ".join([author.name for author in self.authors.all()])
        
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Register(TimeStampedModel, models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, null=False, blank=False)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Register'
        verbose_name_plural = 'Registrations'

class Comment(TimeStampedModel, models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Commnent'
        verbose_name_plural = 'Comments'

class UserProfile(TimeStampedModel, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, blank=False)
    bio = models.TextField(null=False, blank=False)
    mobile = models.TextField(default='Your Mobile Phone Number')
    address = models.TextField(default='Your Address', null=False, blank=False)
    userpicture = models.ImageField(upload_to="my_profile/%Y/%m/%d", null=False, blank=False)
    status = models.TextField(default="Great to have someone to lean on", null=False, blank=False)


class Location(TimeStampedModel, models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='gps')
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'