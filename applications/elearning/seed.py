from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from django.contrib.auth.models import User

Course.objects.all().delete()
Register.objects.all().delete()
Comment.objects.all().delete()
UserProfile.objects.all().delete()
Location.objects.all().delete()
User.objects.all().delete()
from mixer.backend.django import mixer
import random

mixer.cycle(15).blend(User)
mixer.cycle(30).blend(
	Course, author		=	mixer.SELECT, 
	number_of_minutes	=	random.randint(1,9)
	)
#bug here Mixer create way more users that I wanted
mixer.cycle(60).blend(Register, course=mixer.SELECT, student=mixer.SELECT)
mixer.cycle(60).blend(Comment, course=mixer.SELECT, author=mixer.SELECT)


users = User.objects.all()
for user in users:
	mixer.blend(UserProfile, user=user)
	mixer.blend(Location, user=user)

	