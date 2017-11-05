from django.shortcuts import render

# Create your views here.

def index(request, template="wasisi/index.html"):
    """
    Renders the view for the main page
    :param request: the request that initiated this action
    :param template: the template that used for the rendering
    """
    page_data={}
    return render(request,template,page_data)
