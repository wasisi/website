# urls.py
from django.conf.urls import url


from .views import graph, play_count_by_month

#from . import views


urlpatterns = [
    #url(r'^graph/chart/$', views.graph, name='graph'),
    url(r'^graph/chart/$', graph),
    url(r'^play_count_by_month', play_count_by_month, name='play_count_by_month'),
]
