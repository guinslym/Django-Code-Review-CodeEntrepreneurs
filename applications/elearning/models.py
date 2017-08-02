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
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from utils.models_utils import custom_slugify

from autoslug import AutoSlugField
from django.utils.text import slugify

#other package
from vote.models import VoteModel

from utils.models_utils import TimeStampedModel

# Create your models here.
class Course(TimeStampedModel, VoteModel, models.Model):
    author              = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='teacher')
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
    slug                = AutoSlugField(slugify=custom_slugify, 
                            populate_from=lambda instance: instance.author.profile.fullname + " " + instance.title, 
                            unique_with=('created', 'author')
                            )
    price               = models.DecimalField(
                            max_digits=16, decimal_places=2, default=5)
    number_of_minutes   = models.PositiveIntegerField(
                            validators=[
                            MinValueValidator(12)
                            ]
        )

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return '\nid\t\t:{}\ntitle\t\t:{}\nslug\t\t:{}\nshortdesc\t:{}\n'.format(
            self.id, self.title ,self.slug, self.shortdesc[:5]
            )

    def get_absolute_url(self):
        return reverse('elearning:course_detail', args=(self.slug,))

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
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Register'
        verbose_name_plural = 'Registrations'

    @property
    def student_alregistered(self, user):
        return Register.objects.create(
            course= self,
            student= user
            )

class Comment(TimeStampedModel, models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Commnent'
        verbose_name_plural = 'Comments'

class UserProfile(TimeStampedModel, models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name='profile'
        )
    nickname = models.CharField(max_length=50, blank=False)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    bio = models.TextField()
    slug = models.SlugField()
    mobile = models.TextField(default='Your Mobile Phone Number')
    address = models.TextField(default='Your Address', null=False, blank=False)
    userpicture = models.ImageField(upload_to="my_profile/%Y/%m/%d", null=False, blank=False)
    
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '\nid\t\t:{}\nfullname\t:{}, {}\n'.format(
            self.id, self.firstname, self.lastname
            )

    @property
    def fullname(self):
        return (self.firstname + ", " + self.lastname)

    def get_absolute_url(self):
        return reverse('elearning:userprofile_detail', args=(self.slug,))

    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

class Location(TimeStampedModel, models.Model):
    user =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gps')
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    
    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class BankAccount(TimeStampedModel, models.Model):
    user =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bank')
    balance = models.DecimalField(
                            max_digits=16, 
                            decimal_places=2, 
                            default=5)
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '\nid\t\t:{}\nbalance\t\t:$ {}\nusername\t:{}\n'.format(
            self.id, self.balance, self.user.username
            )

    def get_absolute_url(self):
        return reverse('elearning:bank_account_detail', args=(self.id,))

    class Meta:
        ordering = ["-created"]
        #ordering = ("?",)
        verbose_name = 'BankAcount'
        verbose_name_plural = 'BankAccounts'


def course_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.title = instance.title.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title)

def userprofile_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.nickname = instance.nickname.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.nickname)


pre_save.connect(course_pre_save_receiver, sender=Course)
pre_save.connect(userprofile_pre_save_receiver, sender=UserProfile)

