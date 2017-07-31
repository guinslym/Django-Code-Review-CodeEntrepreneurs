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
                               
MVP model tests --- it's not extensive                               

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
        assert obj.id
        assert obj.shortdesc
        assert obj.slug
        assert obj.price
        assert obj.number_of_minutes
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
    def test_an_user_can_LIKE_a_course(self):
        user = mixer.blend(User, username='nickelback')
        course = mixer.blend('elearning.Course', author=user)
        course.votes.up(user.id)
        assert course.votes.count() == 1

    def test_an_user_can_REGISTER_to_a_course(self):
        user = mixer.blend(User, username='nickelback')
        course = mixer.blend('elearning.Course', author=user)
        registered = mixer.blend('elearning.Register',
                         student=user, course=course)
        assert registered.student.username == 'nickelback'

        users = mixer.cycle(10).blend(User, username=mixer.sequence(lambda c: "nickelback_%s" % c))
        
        #registrering 10 users into a course
        for this_user in users:
            registered = mixer.blend('elearning.Register',
                student=this_user, course=course)
        
        #how many Student this Course contains
        assert  Register.objects.filter(course= course.id).count() == 11

    def test_user_can_FOLLOW_a_user(self):
        from friendship.models import Friend, Follow

        user1 = mixer.blend(User, username='nickelback1')
        user2 = mixer.blend(User, username='nickelback2')
        following = Follow.objects.add_follower(user2, user1)
        #import pdb; pdb.set_trace()
        
        #List of a user's followers
        assert user2 in Follow.objects.followers(user1) 
        #List of who a user is following
        assert user1 in Follow.objects.following(user2)

    def test_a_course_can_have_many_comments(self):
        user = mixer.blend(User, username='nickelback')
        course = mixer.blend(Course, student=user)
        comments = mixer.cycle(12).blend(Comment, author=user, 
            course=course, comment=mixer.sequence(lambda c: "test_%s" % c))
        assert Comment.objects.filter(course=course).count() == 12
        #TODO a user can post up to 4 comment to a course
        