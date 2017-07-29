from django import forms
from django.forms import ModelForm
from applications.elearning.models import Course

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['picture', 'shortdesc', 'title', 'price', 'number_of_minutes']

