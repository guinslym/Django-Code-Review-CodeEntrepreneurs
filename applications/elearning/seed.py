from mixer.backend.django import mixer
from applications.elearning.models import Course
from applications.elearning.models import Register
from applications.elearning.models import Comment
from applications.elearning.models import UserProfile
from applications.elearning.models import Location
from django.contrib.auth.models import User


mixer.cycle(15).blend(User)
mixer.cycle(30).blend(Course, author=mixer.SELECT)
mixer.cycle(60).blend(Register, course=mixer.SELECT, student=mixer.SELECT)
mixer.cycle(60).blend(Comment, course=mixer.SELECT, author=mixer.SELECT)

users = User.objects.all()
for user in users:
	mixer.blend(Location, user=user)
	mixer.cycle(40).blend(UserProfile, user=user)
	mixer.cycle().blend(Location, user=user)