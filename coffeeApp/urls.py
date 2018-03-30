#coffeeapp/urls.py

from django.conf.urls import url

from coffeeApp import views


from .views import graph, play_count_by_month, transaction_detail, transaction_like, transaction_list

#from . import views
app_name = 'coffeeApp'
urlpatterns = [
    #url(r'^graph/chart/$', views.graph, name='graph'),
    url(r'^graph/chart/$', graph),
    url(r'^play_count_by_month', play_count_by_month, name='play_count_by_month'),
    url(r'^detail/(?P<id>\d+)/$', transaction_detail, name='transaction_detail'),
    url(r'^like/$', transaction_like, name='like_transaction'),
    url(r'^transactions/list/$', transaction_list.as_view(), name='transaction_list'),
]
