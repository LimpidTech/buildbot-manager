from pyramid.view import view_config
from .. import interfaces

dashboard_arguments = {
    'request_method': 'GET',
    'renderer': 'dashboard.html',
    'context': interfaces.IBuildBotManagerRoot
}

@view_config(**dashboard_arguments)
@view_config(name='dashboard', **dashboard_arguments)
def dashboard(request):
    return {}
