from django.shortcuts import render
from .apps import MainappConfig

# BA: not sure we need to have these here
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Renders the view for the main page
    :param request: the request that initiated this action
    :param template: the template that used for the rendering
    """
    page_data={"page_title":MainappConfig.index_page_name,"show_carousel":True}
    return render(request,MainappConfig.index_page_view_tmpl,page_data)
    
    
def about(request):
    return render(request, 'wasisi/about.html')    

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact us, please email on.','oasis@wasisivillage.com']})    
