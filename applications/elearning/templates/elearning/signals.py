from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

#https://github.com/search?utf8=%E2%9C%93&q=language%3Apython+post_save+profile&type=Code


def create_profile(sender, **kwargs):
	""" Create a profile on post_save signal of User object. """
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = UserProfile(user=user)
		user_profile.save()

post_save.connect(create_profile, sender=User)