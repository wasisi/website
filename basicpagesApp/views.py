from django.shortcuts import render
from .models import Page
from django.utils import timezone
# Create your views here.

def page(request):
	basic_page = Page.objects.all() #basic_page declared in about.html, Page is the class
	return render(request, 'wasisi/about.html', {'basic_page':basic_page})
