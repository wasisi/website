# ContactApp/urls.py
from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact/$', views.contactView, name='contact'),
    url(r'^success/$', views.successView, name='success'),
]