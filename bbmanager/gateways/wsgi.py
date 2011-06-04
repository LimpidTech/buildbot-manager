from pyramid.config import Configurator
from . import portability
from ..resources.resource import Resource

def factory(global_config, **settings):
    """ Application entry point factory for serving as a WSGI application.
    
    Application entry point. Provides a WSGI gateway to our application, so that
    WSGI-compliant applications can make use of it.

    """

    config = Configurator(settings=settings, root_factory=Resource.factory)
    config.include(portability.include_me)

    return config.make_wsgi_app()
