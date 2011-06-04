from zope.interface import implements
from . import resource
from .. import interfaces

class Root(resource.Resource):
    implements(interfaces.IBuildBotManagerRoot)
