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

"""

___  ___          _      _     
|  \/  |         | |    | |    
| .  . | ___   __| | ___| |___ 
| |\/| |/ _ \ / _` |/ _ \ / __|
| |  | | (_) | (_| |  __/ \__ \
\_|  |_/\___/ \__,_|\___|_|___/
                               
                               

"""
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

class TestUserProfile(TestCase):
    def test_init(self):
        obj = mixer.blend('elearning.UserProfile')
        assert obj.pk == 1, 'Should save an instance'

    def test_right_instance(self):
        obj = mixer.blend('elearning.UserProfile')
        assert isinstance(obj, UserProfile) , 'Should be a UserProfile instance'

    def test_count_object(self):
        obj = mixer.cycle(10).blend('elearning.UserProfile')
        assert UserProfile.objects.all().count() == 10
   
    def test_attributes_of_models(self):
        obj = mixer.blend('elearning.UserProfile')
        assert obj.user
        assert obj.nickname
        assert obj.bio
        assert obj.mobile
        assert obj.address
        assert obj.userpicture
        assert obj.status
        # ...

    def test_relation_has_a_user(self):
        user = mixer.blend(User, username='nickelback')
        obj = mixer.blend('elearning.UserProfile', author=user)
        self.assertTrue(obj.author.username, 'nickelback')

"""

______     _       _   _                 _     _           
| ___ \   | |     | | (_)               | |   (_)          
| |_/ /___| | __ _| |_ _  ___  _ __  ___| |__  _ _ __  ___ 
|    // _ \ |/ _` | __| |/ _ \| '_ \/ __| '_ \| | '_ \/ __|
| |\ \  __/ | (_| | |_| | (_) | | | \__ \ | | | | |_) \__ \
\_| \_\___|_|\__,_|\__|_|\___/|_| |_|___/_| |_|_| .__/|___/
                                                | |        
                                                |_|        

"""

class TestRelationship(object):
    """TestRelationship"""
    def test_user_can_LIKE_a_course(self):
        assert True 

    def test_user_can_REGISTER_to_a_course(self):
        assert True 

    def test_user_can_FOLLOW_a_user(self):
        assert True 
        