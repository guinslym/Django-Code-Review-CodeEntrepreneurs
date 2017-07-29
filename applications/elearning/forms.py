from django import forms
from django.forms import ModelForm
from applications.elearning.models import Course
from applications.elearning.models import UserProfile

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['picture', 'shortdesc', 'title', 'price', 'number_of_minutes']

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['nickname', 'bio', 'mobile', 'address', 'userpicture']

