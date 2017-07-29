from django.http.response import HttpResponseForbidden

class UserRequiredMixin(object):
    #for Comment
    #for Register
    #for Location
    #for Profile
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            #add a message here (see DeleteView)
            #add a redirect instead of ResponseForbidden
            #this mixin only works with Author
            return HttpResponseForbidden()

        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)


class UserRequiredMixin(object):
    #for Course
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            #add a message here (see DeleteView)
            #add a redirect instead of ResponseForbidden
            #this mixin only works with Author
            return HttpResponseForbidden()

        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)

