from braces.views import LoginRequiredMixin, PermissionRequiredMixin, \
    CsrfExemptMixin, JsonRequestResponseMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView

class AuthorMixin(object):
    def by_author(self, name):
        return self.filter(author=name)

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    template_name = 'courses/manage/course/form.html'



"""
Advanced
"""
class RolesRequiredMixin(object):
    """
    A django View mixin that checks if the user has got the roles which are specified as an attribute of the class.
    :required_roles: An iterable of strings with role names.
    """
    required_roles = None

    def has_roles(self):
        """
        Checks if the user has a the roles as specified by the `required_roles` class attribute.
        :return: `True` if check passes; `False` if the user did not pass all requirements.
        """
        user = self.request.user
        roles = self.required_roles
        if not roles:
            raise NotImplementedError(
                _('{0} is missing the "required_roles" attribute.').format(self.__class__.__name__)
            )
        for role in roles:
            check = user.has_role(role)
            if not check:
                return False
        return True

    def handle_insufficient_roles(self, request, *args, **kwargs):
        """
        Rediredt the user to the page he came from and
        show a message pointing him to the game to unlock more features.
        :return: The page the user came from or his home.
        """
        user = request.user
        if user.is_superuser:
            message = _('Viewing as {}.'.format('admin'))
            messages.info(request, message)
            return super().dispatch(request, *args, **kwargs)
        else:
            message = _('You currently do not have the required roles.')
            messages.warning(request, message)
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        has_roles = self.has_roles()
        if not has_roles:
            return self.handle_insufficient_roles(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)






class OwnerRequiredMixin(object):
    """
    A django View mixin that checks if the user has got ownership of the resource.
    """

    def has_ownership(self):
        """
        Checks if the user is the owner of the resource.
        :return: `True` if check passes; `False` if the user did not pass all requirements.
        """
        user = self.request.user
        object = self.get_object()
        if object.owned_by(user):
            return True
        else:
            return False

    def handle_no_ownership(self, request, *args, **kwargs):
        """
        Rediredt the user to the page he came from and
        show a message informing him of the lack of ownership.
        :return: The page the user came from or his home.
        """
        user = request.user
        if user.is_superuser:
            message = _('Viewing as {}.'.format('admin'))
            messages.info(request, message)
            return super().dispatch(request, *args, **kwargs)
        else:
            message = _('Ownership required.')
            messages.warning(request, message)
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def dispatch(self, request, *args, **kwargs):
        ownership = self.has_ownership()
        if not ownership:
            return self.handle_no_ownership(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
