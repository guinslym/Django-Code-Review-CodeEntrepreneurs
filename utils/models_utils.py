from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.utils.text import slugify
import random
import string

#model_utils.models

class AutoCreatedField(models.DateTimeField):
    """
    A DateTimeField that automatically populates itself at
    object creation.
    By default, sets editable=False, default=datetime.now.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)

class AutoLastModifiedField(AutoCreatedField):
    """
    A DateTimeField that updates itself on each save() of the model.
    By default, sets editable=False and default=datetime.now.
    """
    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value
                
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    class Meta:
        abstract = True


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, my_chosen_field='slug'):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug = slugify(my_chosen_field)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "CodeReview-{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=10)
                )
        return unique_slug_generator(instance)
    return slug
