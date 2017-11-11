from django.shortcuts import render
from .apps import MainappConfig

# Create your views here.

def index(request):
    """
    Renders the view for the main page
    :param request: the request that initiated this action
    :param template: the template that used for the rendering
    """
    page_data={"page_title":MainappConfig.index_page_name}
    return render(request,MainappConfig.index_page_view_tmpl,page_data)
