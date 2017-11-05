from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request,template='uploadApp/index.html'):
    """
    Serves the view for loading a dataset. This view
    requires the user to be logged and also be a developer
    :param request: the request that initiated this action
    :param template: the template that used for the rendering
    :return:
    """
    page_data={}

    return render(request,template,page_data)
