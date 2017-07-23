# -*- coding: utf-8 -*-
from datetime import datetime

#Fixture package
from mixer.backend.django import mixer

#Test package & Utils
from django.test import TestCase
import pytest
pytestmark = pytest.mark.django_db

#models
from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from django.contrib.auth.models import User

#url helper
from django.core.urlresolvers import reverse, resolve


class TestCourse(TestCase):
    def test_init(self):
        obj = mixer.blend('elearning.Course')
        assert obj.pk == 1, 'Should save an instance'

    def test_right_instance(self):
        obj = mixer.blend('elearning.Course')
        assert isinstance(obj, Course) , 'Should be a Course instance'

    def test_count_object(self):
        obj = mixer.cycle(10).blend('elearning.Course')
        assert Course.objects.all().count() == 10
   
    def test_attributes_of_models(self):
        obj = mixer.blend('elearning.Course')
        assert obj.author
        assert obj.picture
        # ...

    def test_relation_has_a_user(self):
        user = mixer.blend(User, username='nickelback')
        obj = mixer.blend('elearning.Course', author=user)
        self.assertTrue(obj.author.username, 'nickelback')

    def test_relationship_one_to_many(self):
        """slow test 

        Clue:
           Course.objects.all().prefetch_related('user')
        """
        User.objects.all().delete()
        Course.objects.all().delete()
        user = mixer.blend(User, username='nickelback')
        obj = mixer.cycle(5).blend('elearning.Course', author=user)
        courses = Course.objects.all()
        for i in courses:
            self.assertTrue(i.author.username, 'nickleback')