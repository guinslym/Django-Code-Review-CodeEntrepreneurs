from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from applications.elearning.models import Course
from applications.elearning.models import Register

register = template.Library()

@register.filter(needs_autoescape=True, takes_context=True)
def is_registered(context, course):
	user = context['request'].user
	is_it = Register.objects.filter(course=course, student=user)
	if is_it:
		result = '<strong>%s</strong>%s' % (esc('hello'), esc(' world registered'))
		return mark_safe(result)
	else:
		result = '<strong>%s</strong>%s' % (esc('hello'), esc(' world  not registered'))
		return mark_safe(result)