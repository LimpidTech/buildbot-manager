from pyramid.view import view_config

@view_config(name='dashboard', request_method='GET', renderer='dashboard.html')
def dashboard(request):
    return {}
