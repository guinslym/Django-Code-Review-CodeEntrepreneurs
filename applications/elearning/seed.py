from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from django.contrib.auth.models import User
from django.utils.text import slugify
from utils.models_utils import random_string_generator

Course.objects.all().delete()
Register.objects.all().delete()
Comment.objects.all().delete()
UserProfile.objects.all().delete()
Location.objects.all().delete()
User.objects.all().delete()
from mixer.backend.django import mixer
import random


def title():
	courses = ['vuejs', 'reactjs', 'java', 'php','pyramid',
	'python','flask','falcon','docker', 'jquery', 'wordpress']
	course = courses[random.randint(0, 10)]
	return 'Introduction to '+ course.capitalize()


mixer.cycle(15).blend(User)
mixer.cycle(30).blend(
	Course, author		=	mixer.SELECT, 
	number_of_minutes	=	random.randint(1,9),
	title 				=   title()
	)
#bug here Mixer create way more users that I wanted
mixer.cycle(60).blend(Register, course=mixer.SELECT, student=mixer.SELECT)
mixer.cycle(60).blend(Comment, course=mixer.SELECT, author=mixer.SELECT)


users = User.objects.all()
for user in users:
	mixer.blend(UserProfile, user=user)
	mixer.blend(Location, user=user)

	
courses = Course.objects.all()
for i in courses:
	i.title = title()
	i.slug = "CodeReview-" + random_string_generator() + "-" + slugify(i.title) 
	i.save()
	print("{} - {}".format(i.title , i.slug))
