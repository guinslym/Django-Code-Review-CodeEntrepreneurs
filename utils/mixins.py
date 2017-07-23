

class AuthorMixin(object):
    def by_author(self, name):
        return self.filter(author=name)