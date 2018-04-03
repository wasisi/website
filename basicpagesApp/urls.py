from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'node/(?P<basic_page>[-\w]+)/$', views.page, name='page'),
]
