class Resource(object):
    request = None

    __parent__ = None
    __name__ = None

    def __init__(self, request, name=None, parent=None):
        self.request = request

        self.__name__ = name
        self.__parent__ = parent

    def __getitem(self, name):
        raise KeyError()

    @classmethod
    def factory(object_class, *args, **kwargs):
        return object_class(*args, **kwargs)
