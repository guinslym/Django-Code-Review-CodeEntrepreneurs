from django import forms
from django.forms import ModelForm
from applications.elearning.models import Course
from applications.elearning.models import UserProfile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['nickname', 'bio', 'mobile', 'address', 'userpicture']

class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('shortdesc'),
            Field('title'),
            Field('price'),
            Field('number_of_minutes'),
            Submit('submit', 'submit', css_class="btn-success"),
            )

    class Meta:
        model = Course
        fields = ['picture', 'shortdesc', 'title', 'number_of_minutes', 'price']
