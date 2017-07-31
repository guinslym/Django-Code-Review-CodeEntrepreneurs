from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

"""
TODO: this doen't work 
purpose : create a profile when the user just SignUp


All my signals doens't seems to work include the one in the Models.py
"""
def create_profile(sender, **kwargs):
	""" Create a profile on post_save signal of User object. """
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = UserProfile(user=user)
		user_profile.save()

post_save.connect(create_profile, sender=User)