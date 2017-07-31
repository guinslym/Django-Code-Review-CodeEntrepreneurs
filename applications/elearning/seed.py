"""
	only for seeding the database

	COPY-And-PASTE to shell
	python manage.py shell_plus

	make sure you did pip install the requirements
"""

from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from applications.elearning.models import BankAccount
from django.contrib.auth.models import User
from django.utils.text import slugify
from utils.models_utils import random_string_generator

from faker import Factory
fake = Factory.create()

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
	title 				=   title(),
	price				=   random.randint(1,10),
	)
#bug here Mixer create way more users that I wanted
mixer.cycle(60).blend(Register, course=mixer.SELECT, student=mixer.SELECT)
mixer.cycle(60).blend(Comment, course=mixer.SELECT, author=mixer.SELECT)


import random
users = User.objects.all()
for user in users:
	bank = mixer.blend(BankAccount, user=user)
	bank.balance = random.randint(3,12)
	bank.save()
	
courses = Course.objects.all()
for i in courses:
	i.title = title()
	i.slug = "CodeReview-" + random_string_generator(size=10) + "-" + slugify(i.title) 
	i.shortdesc = fake.text(300)
	i.price = random.randint(1,10)
	i.number_of_minutes = random.randint(18,59)
	i.save()
	print("{} - {}".format(i.title , i.slug))


profiles = UserProfile.objects.all()
for i in profiles:
	i.slug = "CodeReview-User-" + random_string_generator(size=6) + "-" + slugify(i.fullname) 
	i.bio = fake.text(300)
	i.save()
	print("{} - {} - {}".format(i.firstname, i.lastname, i.slug))



