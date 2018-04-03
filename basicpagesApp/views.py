from django.shortcuts import render, get_object_or_404
from .models import Page
from django.utils import timezone

# Create your views here.

def page(request, basic_page):
	basic_page =  get_object_or_404(Page, slug=basic_page) #basic_page declared in about.html, Page is the class
	return render(request, 'wasisi/basic.html', {'basic_page':basic_page})
