from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from applications.elearning.models import Course
from applications.elearning.models import Register

register = template.Library()

@register.simple_tag
def has_voted(course_slug, user):
	course = Course.objects.filter(slug=course_slug).get()
	user_id = user.id
	if course in Course.votes.all(user_id):
		return "fa-thumbs-o-down"
	else:
		return 'fa-thumbs-o-up'


@register.simple_tag
def total_vote(course_slug):
	course = Course.objects.filter(slug=course_slug).get()
	return course.votes.count()


@register.simple_tag
def is_registered(course_slug, user=None):
	course = Course.objects.filter(slug=course_slug).get()
	reg = Register.objects.filter(student=user, course=course)
	#import pdb; pdb.set_trace()
	if len(reg) == 0:
		return 'Register'
	else:
		return 'UnRegister'